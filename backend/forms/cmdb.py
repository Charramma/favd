#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/2/22 18:38
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: cmdb.py
# @Software: PyCharm

from wtforms import Form, StringField, validators, TextAreaField
from wtforms.validators import DataRequired, email, length, ValidationError
from tools.error_code import FormValidateException


class IDCForm(Form):
    idc_name = StringField('idc名称', validators=[DataRequired(message='idc名不能为空')])
    region = StringField('idc所属区域', validators=[DataRequired(message='idc所属区域不能为空')])
    idc_supplier = StringField('idc供应商', validators=[DataRequired(message='idc供应商不能为空')])
    administrator = StringField('管理员', validators=[DataRequired(message='管理员不能为空')])
    administrator_phone = StringField('管理员电话', validators=[DataRequired(message='管理员电话不能为空'), length(min=11, max=11, message='电话号码格式异常')])
    administrator_email = StringField('管理员邮箱', validators=[DataRequired(message='管理员邮箱不能为空'), email(message='请输入有效的邮箱地址')])
    bandwidth = StringField('机房带宽')
    ip_address_range = StringField('IP地址段', validators=[DataRequired(message='IP地址段不能为空')])
    description = TextAreaField('描述信息')