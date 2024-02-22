#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/2/22 18:38
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: cmdb.py
# @Software: PyCharm

from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired, email, length, ValidationError
from tools.error_code import FormValidateException


class IDCForm(Form):
    pass