from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, email, length, ValidationError
from models.user import UserProfile
from werkzeug.security import check_password_hash
from libs.error_code import AuthorizedException
import re


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), email(message="邮箱不合法")])
    password = StringField(validators=[DataRequired(), length(min=8, max=16, message="密码长度不符合要求")])
    username = StringField(validators=[DataRequired(), length(min=4, message="用户名不能少于4个字符")])
    mobile = StringField()

    # 自定义字段检查
    def validate_email(self, value):
        """验证email是否在数据库中已存在"""
        if UserProfile.query.filter_by(user_profile_email=value.data).first():
            raise ValidationError("邮箱已存在")

    def validate_password(self, value):
        """验证密码是否同时包含大小写字母、数字和特殊符号"""
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', value.data):
            raise ValidationError('密码必须包含至少8个字符，其中包括一个字母、一个数字和一个特殊字符。')


class LoginForm(Form):
    # 这里用这个名字接收数据是由于前端iview-admin使用的是这个名字，在那边修改成本比较大，因此改这边
    userName = StringField(validators=[DataRequired(), email(message="邮箱不合法")])
    password = PasswordField(validators=[DataRequired()])

    def validate(self):
        # 验证用户名密码(如果是由于邮箱不合法导致还是会提示用户名密码错误，考虑如何优化)
        super().validate()

        user = UserProfile.query.filter_by(user_profile_email=self.userName.data).first()
        # check_password_hash对hash加密的密码与明文的密码进行比较
        if user and check_password_hash(user.password, self.password.data):
            return user
        else:
            raise AuthorizedException(message="用户名或密码错误")
