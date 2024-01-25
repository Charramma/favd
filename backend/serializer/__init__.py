#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/10 11:11
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: __init__.py
# @Software: PyCharm

from .extension import ma


def init_app(app):
    ma.init_app(app)