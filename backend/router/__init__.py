#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:46
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: __init__.py
# @Software: PyCharm

from .views import bp
from .v1 import v1_bp


def init_app(app):
    app.register_blueprint(bp)
    app.register_blueprint(v1_bp)