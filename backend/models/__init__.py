#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:55
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: __init__.py
# @Software: PyCharm

from .extension import db
from flask_migrate import Migrate


def init_app(app):
    db.init_app(app)
    migrate = Migrate(app, db)
