#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Author: AnhNT
    Company: MobioVN
    Date created: 26/02/2021

"""
from .config import SystemConfigKeys
from .http_jwt_auth import ProjectAuthorization, TYPICALLY
from flask import json, request
from jose import jwt
from mobio.libs.Singleton import Singleton
# from mobio.sdks.license import MobioLicenseSDK
import re


@Singleton
class MobioAuthorization(ProjectAuthorization):
    def __init__(self):
        self.key = None
        self.algorithm = None
        self.options = {
            "verify_signature": True,
            "verify_aud": False,
            "verify_iat": False,
            "verify_exp": True,
            "verify_nbf": False,
            "verify_iss": False,
            "verify_sub": False,
            "verify_jti": False,
        }
        self.local_redis = None

    @classmethod
    def __merchant_id__(cls, jwt_token=None):
        merchant_id = cls.get_value_from_decode_base64("merchant_id", jwt_token)
        if not merchant_id:
            merchant_id = request.headers.get(SystemConfigKeys.X_MERCHANT_ID, None)  # from Mobile
        if not merchant_id:
            print("admin_sdk:: __merchant_id__ None")
        return merchant_id

    @staticmethod
    def get_value_from_decode_base64(key, jwt_token):
        result = None
        if not key or not jwt_token:
            return result
        try:
            from .utils import Base64
            b_json = json.loads(Base64.decode(jwt_token.split(".")[1]))
            result = b_json.get(key, None)
        except Exception as e:
            print("admin_sdk:: get_value_from_decode_base64 error: {}, jwt_token: {}".format(e, jwt_token))
        return result

    @staticmethod
    def get_auth_info(merchant_id):
        from .utils import ConfigJWT

        auth_info = ConfigJWT().get_config_auth(merchant_id)
        return (
            auth_info[SystemConfigKeys.JWT_SECRET_KEY],
            auth_info[SystemConfigKeys.JWT_ALGORITHM],
        )

    @staticmethod
    def get_auth_anonymous(merchant_id):
        from .utils import ConfigJWT

        auth_info = ConfigJWT().get_config_anonymous(merchant_id)
        return (
            auth_info.get("secret_key"),
            auth_info.get("algorithm"),
        )

    @classmethod
    def get_jwt_info(cls):
        return cls.get_auth_info(cls.__merchant_id__())

    def get(self, token, field_name):
        """
        lấy thông tin theo tên trường từ Json Web Token
        :param token:
        :param field_name:
        :return:
        """
        try:
            merchant_id = self.__merchant_id__(token)
            jwt_type = self.get_value_from_decode_base64("jwt_type", jwt_token=token)
            if jwt_type == "anonymous":
                secret_key, algorithm = self.get_auth_anonymous(merchant_id)
            else:
                secret_key, algorithm = self.get_auth_info(merchant_id)
                self.key = secret_key
                self.algorithm = algorithm
            body = self._decode(token, secret_key=secret_key, algorithm=algorithm)
            return body.get(field_name, None) if body else None
        except Exception as e:
            self.key = None
            self.algorithm = None
            print("admin_sdk::get key in token: {} ; field_name: {}, err: {}".format(token, field_name, str(e)))
            raise ValueError("get key in token: {}".format(e))

    def _encode(self, body):
        try:
            return jwt.encode(body, self.key, self.algorithm)
        except Exception as e:
            print("admin_sdk::can not encode token: {} ; key: {}, algorithm: {}".format(
                str(e), self.key, self.algorithm))
            return None

    def _decode(self, body, secret_key=None, algorithm=None):
        if not secret_key and not algorithm:
            secret_key = self.key
            algorithm = self.algorithm
        try:
            return jwt.decode(body, secret_key, algorithm, self.options)
        except Exception as e:
            print("admin_sdk::can not decode token: {} ; key: {}, algorithm: {}".format(
                str(e), secret_key, algorithm))
            return None

    def is_permitted(self, jwt_token, typically, method):
        """
        hàm kiểm tra method có được phân quyền hay không
        :param jwt_token:
        :param typically:
        :param method:
        :return:
        """
        return True

    def verify_token(self, jwt_token, typically):
        """
        nếu là module có chức năng au then thì kiem tra trong redis
        nếu là module khác thì gọi moddule authen để verify token
        :param typically:
        :param jwt_token:
        :return: trả về token nếu hợp lệ
        """
        try:
            from .utils import check_basic_auth_v2

            # if MobioAuthorization.license_merchant_expire():
            #     return None

            if typically == TYPICALLY.BEARER or typically == TYPICALLY.DIGEST:
                jwt_type = self.get(jwt_token, "jwt_type")
                if jwt_type == "anonymous":
                    return jwt_token
                else:
                    arr_token = jwt_token.split(".")
                    # kiểm tra token trong REDIS
                    verify_token = arr_token[2]
                    value = self.local_redis.get(verify_token)
                    if not value:
                        print("admin_sdk::verify_token: {} not found in redis".format(verify_token))
                        return None
                    return jwt_token

            elif typically == TYPICALLY.BASIC:
                if not check_basic_auth_v2(jwt_token):
                    print("admin_sdk:: {} basic key invalid".format(jwt_token))
                    return None
                    # if not MobioAuthorization.check_app_data_out(jwt_token):
                    #     raise ValueError("admin_sdk:: {} basic key invalid".format(jwt_token))
                return jwt_token

        except Exception as e:
            print("admin_sdk::MobioAuthorization::verify_token: ERROR: {}".format(e))
        return None
    
    def get_jwt_value(self, key):
        try:
            auth_type, token = request.headers["Authorization"].split(None, 1)
            return self.get(token, key)
        except Exception as err:
            print("admin_sdk::get_jwt_value err: {}, key: {}".format(err, key))
            return None

    # @staticmethod
    # def license_merchant_expire():
    #     from .utils import get_list_parent_merchant
    #     merchant_expire = True
    #     try:
    #         x_merchant_id = request.headers.get(SystemConfigKeys.X_MERCHANT_ID)
    #         if not x_merchant_id:
    #             print("admin_sdk::check_time_merchant_expire X-Merchant-ID not found")
    #         else:
    #             data_parent = get_list_parent_merchant(merchant_id=x_merchant_id,
    #                                                    token_value=SystemConfigKeys.MOBIO_TOKEN)
    #             if data_parent and data_parent.get("data") and len(data_parent.get("data")) > 0:
    #                 root_merchant_id = data_parent.get("data")[0].get("root_merchant_id")
    #                 if root_merchant_id:
    #                     merchant_expire = MobioLicenseSDK().merchant_has_expired(
    #                         root_merchant_id
    #                     )
    #                 else:
    #                     print("admin_sdk::check_time_merchant_expire root_merchant_id not found")
    #             else:
    #                 print("admin_sdk::check_time_merchant_expire parent merchant not found")
    #
    #     except Exception as e:
    #         print("admin_sdk::check_time_merchant_expire: ERROR: %s" % e)
    #     return merchant_expire

    @staticmethod
    def check_app_data_out(app_id):
        from .utils import get_list_api_register_app
        merchant_id = request.headers.get(SystemConfigKeys.X_MERCHANT_ID)
        if not merchant_id:
            return False
        list_api = get_list_api_register_app(merchant_id, app_id)
        if not list_api:
            return False
        path_query = request.path
        method = request.method.lower()
        for item in list_api:
            if method == item.get("method") and item.get("path_regex"):
                pattern_path = re.compile(item.get("path_regex"))
                if bool(pattern_path.match(path_query)):
                    return True
        return False

    @classmethod
    def check_anonymous_permissions(cls, jwt_token):
        # VD path: a = "/tag/api/v1.0/tags/(.*)/list"
        permissions = cls.get_value_from_decode_base64("permissions", jwt_token)
        if isinstance(permissions, dict):
            path_query = request.path
            method = request.method.lower()
            if permissions.get(path_query) and method in permissions.get(path_query):
                return True
            # check pattern neu co
            for k, v in permissions.items():
                pattern_path = re.compile(k)
                if bool(pattern_path.match(path_query)) and method in v:
                    return True
        return False



