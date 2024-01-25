#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 17:41
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: enums.py
# @Software: PyCharm

import enum


# class AssetType(enum.Enum):
#     SERVER = 1
#     NETWORK = 2
#
#
# class StatusType(enum.Enum):
#     INIT = 0
#     ONLINE = 1
#     OFFLINE = 2
#     UNREACHABLE = 3
#     MAINTAIN = 4


class MethodType(enum.Enum):
    GET = 1
    POST = 2
    DELETE = 3
    PUT = 4
    PATCH = 5