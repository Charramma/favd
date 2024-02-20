#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/5 16:59
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: v1.py
# @Software: PyCharm

from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, email, length, ValidationError
from models.user import UserProfile
from werkzeug.security import check_password_hash, generate_password_hash
from tools.error_code import AuthorizedException
import re


# 登录表单类
class LoginForm(Form):
    userName = StringField('邮箱', validators=[DataRequired(message='邮箱不能为空'), email(message="请输入有效的邮箱地址")])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])

    def validate(self, extra_validators=None):
        super().validate()

        user = UserProfile.query.filter_by(user_profile_email=self.userName.data).first()
        if not user:
            raise AuthorizedException(message="用户不存在")
        if user and check_password_hash(user.password, self.password.data):
            # 如果用户存在，检查输入的密码与库中密码是否一致
            return user
        else:
            raise AuthorizedException(message="用户名或密码输入错误")


# 注册表单类
class RegisterForm(Form):
    userName = StringField('用户名', validators=[DataRequired(message='用户名不能为空'), length(min=4, message='用户名不能少于4个字符')])
    email = StringField('邮箱地址', validators=[DataRequired(), email(message="请输入有效的邮箱地址")])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空'), length(min=8, max=16, message="密码长度必须在8到16位之间")])


    def validate_email(self, value):
        """验证邮箱是否已存在"""
        if UserProfile.query.filter_by(user_profile_email=value.data).first():
            raise ValidationError('该邮箱已被注册')

    def validate_password(self, value):
        """验证密码是否同时包含大小写字母、数字和特殊符号"""
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', value.data):
            raise ValidationError('密码必须包含至少8个字符，其中包括一个字母、一个数字和一个特殊字符。')


# 修改密码表单类
class ChangePasswordForm(Form):
    old_password = PasswordField('旧密码', validators=[DataRequired(message='旧密码不能为空')])
    new_password = PasswordField('新密码', validators=[DataRequired(message='新密码不能为空'), length(min=8, max=16, message="密码长度必须在8到16位之间")])

    def validate_new_password(self, value):
        """验证新密码是否符合要求"""
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', value.data):
            raise ValidationError('密码必须包含至少8个字符，其中包括一个字母、一个数字和一个特殊字符。')