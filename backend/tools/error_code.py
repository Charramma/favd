#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/8 9:54
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: error_code.py
# @Software: PyCharm
# @Description: 自定义异常类

from werkzeug.exceptions import HTTPException
import json


class APIException(HTTPException):
    code = 500  # http返回码
    message = "opps!"  # 异常信息
    status_code = 9999  # 业务状态码

    def __init__(self, message=None, code=None, status_code=None, headers=None):
        if code:
            self.code = code
        if status_code:
            self.status_code = status_code
        if message:
            self.message = message
        # super().__init__(description=msg)
        super().__init__(message, None)

    def get_body(self, environ=None, *args, **kwargs):
        return json.dumps({"code": self.status_code, "message": self.message})

    def get_headers(self, environ=None, *args, **kwargs):
        return [("Content-Type", "application/json")]


class PermissionDeny(APIException):
    message = "用户没有权限"
    status_code = 10006
    code = 403


class APIAuthorizedException(APIException):
    message = "用户认证失败"
    status_code = 10004
    code = 401


class FormValidateException(APIException):
    """自定义异常类测试"""
    message = "表单验证失败"
    status_code = 10002


class ArgsTypeException(APIException):
    message = "参数传递方式不正确"
    status_code = 10003


class AuthorizedException(APIException):
    message = "用户认证失败"
    status_code = 10001
    code = 401


class Success(object):
    message = "OK"
    status_code = 10000
    code = 200


class DataNotFoundException(APIException):
    message = "查询的数据不存在"
    status_code = 10005
    code = 404


class DatabaseOperationException(APIException):
    message = "数据库操作异常"
    status_code = 10007
    code = 500