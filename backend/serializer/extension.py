#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/10 11:16
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: extension.py
# @Software: PyCharm

from flask_marshmallow import Marshmallow

ma = Marshmallow()

from . import user_serializer
from . import ops_tools_serializer
