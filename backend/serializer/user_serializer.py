#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/1/10 11:24
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: user_serializer.py.py
# @Software: PyCharm

from models.user import UserProfile
from .extension import ma


class UserSchema(ma.Schema):
    class Meta:
        model = UserProfile
        fields = ('user_profile_id', 'user_profile_name', 'user_profile_email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
