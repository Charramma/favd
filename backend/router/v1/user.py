#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/29 16:50
# @Author: Charramma
# @E-Mail: huang.zyn@qq.com
# @File: v1.py
# @Software: PyCharm

from tools.nestable_blueprint import NestableBlueprint
from flask_restful import Api, Resource
from flask import request, g, jsonify
from tools.error_code import ArgsTypeException, FormValidateException
from forms.user import LoginForm, RegisterForm
from tools.authorize import create_token, auth
from tools.response import generate_response
from models.user import UserProfile
from serializer.user_serializer import user_schema, users_schema
from tools.handler import default_error_handler

user_bp = NestableBlueprint('user_v1', __name__, url_prefix='user')
api = Api(user_bp)

# api.handle_error = default_error_handler


class LoginView(Resource):
    def post(self):
        """用户登录接口"""
        data = request.json  # 接收前端请求中携带的数据
        if not data:
            raise ArgsTypeException(message="参数异常")
        # 通过表单类验证数据合法性
        form = LoginForm(data=data)
        user = form.validate()  # 表单的validate函数返回了合法的数据

        # 生成token
        token = create_token(uid=user.user_profile_id)
        return generate_response(data={"token": token})


class UserView(Resource):
    @auth.login_required
    def get(self):
        """获取用户信息"""
        user = UserProfile.query.get(g.user["uid"])
        return generate_response(data=user_schema.dump(user))


class RegisterView(Resource):
    def post(self):
        """用户注册"""
        data = request.json
        form = RegisterForm(data=data)
        if form.validate():
            UserProfile.create_user(user_profile_name=form.userName.data, user_profile_email=form.email.data,
                                    password=form.password.data)
            user = UserProfile.query.filter_by(user_profile_email=data.get("email")).first()
            result = user_schema.dump(user)

            return generate_response(data=result)
        else:
            result = form.errors
            raise FormValidateException(message=result)


api.add_resource(RegisterView, '/register')
api.add_resource(LoginView, '/login')
api.add_resource(UserView, '/')
