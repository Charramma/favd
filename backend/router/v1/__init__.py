#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:49
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: __init__.py
# @Software: PyCharm

from tools.nestable_blueprint import NestableBlueprint
from .user import user_bp
from .ops_tools import ops_tools_bp

version = 'v1'

v1_bp = NestableBlueprint(version, __name__, url_prefix='/api/v1/')

v1_bp.register_blueprint(user_bp)
v1_bp.register_blueprint(ops_tools_bp)