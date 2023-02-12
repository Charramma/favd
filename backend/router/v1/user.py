"""
用户注册、登录相关接口
"""

from flask import request, g
from libs.nestable_blueprint import NestableBlueprint
from flask_restful import Api, Resource
from libs.handler import default_error_handler
from models.user import UserProfile
from models.extension import db
from libs.error_code import FormValidateException, ArgsTypeException
from libs.authorize import create_token, verify_token
from libs.authorize import auth
from libs.response import generate_response
from serializer.user_serializer import user_schema, users_schema
from forms.user import RegisterForm, LoginForm

user_bp = NestableBlueprint('user_v1', __name__, url_prefix='user')

api = Api(user_bp)

api.handle_error = default_error_handler


class RegisterView(Resource):
    def post(self):
        """用户注册"""
        # 获取用户传过来的数据
        data = request.json
        # 验证参数有效性
        form = RegisterForm(data=data)  # 将表单和数据进行绑定
        if form.validate():
            # 调用模型类方法create_user，将用户信息存入数据库
            UserProfile.create_user(user_profile_email=form.email.data,
                                    user_profile_name=form.username.data,
                                    password=form.password.data,
                                    user_profile_mobile=form.mobile.data)
            user = UserProfile.query.filter_by(user_profile_email=data.get("email")).first()
            result = user_schema.dump(user)

            return generate_response(data=result)
        else:
            result = form.errors
            raise FormValidateException(message=result)


class LoginView(Resource):
    def post(self):
        """用户登录"""
        # 接收用户数据
        data = request.json
        if not data:
            raise ArgsTypeException(message="传参方式不对，或没有传参")
        # 验证数据合法性
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


api.add_resource(RegisterView, '/register/')
api.add_resource(LoginView, '/login/')
api.add_resource(UserView, '/')
