#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/8 10:55
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: response.py
# @Software: PyCharm


from tools.error_code import Success


def generate_response(data=None, message=Success.message,
                      status_code=Success.status_code, **kwargs):
    if data is None:
        data = []
    return {
        "message": message,
        "status_code": status_code,
        "data": data,
        **kwargs
    }
