#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 17:10
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: v1.py
# @Software: PyCharm

from .extension import db
from sqlalchemy import func
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    """用户表"""
    __tablename__ = "user_profile"
    user_profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_profile_name = db.Column(db.String(32), comment="姓名")
    user_profile_email = db.Column(db.String(32), comment="邮箱")
    _password = db.Column("password", db.String(128), comment="密码")

    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        """将密码生成密码hash处理"""
        self._password = generate_password_hash(value)

    def __str__(self):
        return f"<User {self.user_profile_name}>"

    @classmethod
    def create_user(cls, user_profile_email, user_profile_name, password):
        user = cls()
        user.user_profile_name = user_profile_name
        user.user_profile_email = user_profile_email
        user.password = password
        db.session.add(user)
        db.session.commit()
