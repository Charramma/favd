#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:41
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: settings.py
# @Software: PyCharm

DEBUG = True
ENV = "development"
HOST = "0.0.0.0"
PORT = "5000"
JSON_AS_ASCII = False

# 数据库配置
SQLALCHEMY_DATABASE_URI = 'sqlite:///local.db'

# 设置token过期时间
EXPIRES_IN = 3600*24

SECRET_KEY = "bc2b2234c781b3dd8ae04131f1ea35438e4dbda39ecda1392da32d4bdaeec87a"