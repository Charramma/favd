#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:40
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: app.py
# @Software: PyCharm


from flask import Flask
import models
import router
from flask_cors import CORS


def create_app(config=None):
    app = Flask(__name__)

    cors = CORS(app, resource={'*': {'origins': '*'}})

    # 引入配置文件
    app.config.from_object('config.settings')

    # 初始化ORM
    models.init_app(app)

    # 初始化蓝图
    router.init_app(app)

    return app
