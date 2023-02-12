"""
定义用户相关表
"""

from .extension import db
from sqlalchemy import func
from libs.enums import MethodType
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    """用户表"""
    __tablename__ = "user_profile"
    user_profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_profile_name = db.Column(db.String(32), comment="姓名")
    user_profile_email = db.Column(db.String(32), comment="邮箱")
    user_profile_mobile = db.Column(db.String(11), comment="电话号码")
    _password = db.Column("password", db.String(128), comment="密码")
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"))
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    asset = db.relationship('Asset', backref='user_profile')
    api_tokens = db.relationship("APIToken", backref="user_profile")

    # business_units = db.relationship('BusinessUnit', secondary='business_unit_user_profile',
    #                                  back_populates='user_profiles')

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
    def create_user(cls, user_profile_email, user_profile_name, password, user_profile_mobile):
        user = cls()
        user.user_profile_name = user_profile_name
        user.user_profile_email = user_profile_email
        user.password = password
        user.user_profile_mobile = user_profile_mobile
        db.session.add(user)
        db.session.commit()


apitokenpermission = db.Table("api_token_permissions",
                              db.Column("api_token_id", db.Integer, db.ForeignKey("api_token.api_token_id")),
                              db.Column("api_permission_id", db.ForeignKey("api_permission.api_permission_id")),
                              )


class APIToken(db.Model):
    __tablename__ = "api_token"
    api_token_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_token_appid = db.Column(db.String(64), comment='appid')
    api_token_secretkey = db.Column(db.String(255), nullable=False, comment='token')
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.user_profile_id'))
    permissions = db.relationship('APIPermission', secondary=apitokenpermission, backref='api_token')


class APIPermission(db.Model):
    __tablename__ = "api_permission"
    api_permission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_permission_url = db.Column(db.String(128))
    api_permission_method_type = db.Column(db.Enum(MethodType), nullable=False, comment='GET/POST/PUT等HTTP请求方法')
    note = db.Column(db.Text, comment="备注")
    create_at = db.Column(db.DateTime, default=func.now(), comment="创建时间")
    update_at = db.Column(db.DateTime, onupdate=func.now(), comment="修改时间")
    status = db.Column(db.Integer)

    # tokens = db.relationship('APIToken', secondary=apitokenpermission, backref='apipermission')


role_permissions = db.Table(
    "role_permissions",
    db.Column("role_id", db.Integer, db.ForeignKey("role.role_id")),
    db.Column('permission_id', db.Integer, db.ForeignKey("api_permission.api_permission_id"), primary_key=True)
)


class Role(db.Model):
    __tablename__ = "role"
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(128), comment="角色名")
    users = db.relationship("UserProfile", backref="role")
    permissions = db.relationship("APIPermission", secondary=role_permissions, backref="role")
