from libs.nestable_blueprint import NestableBlueprint
from .cmdb import cmdb_bp
from .user import user_bp

version = 'v1'

v1_bp = NestableBlueprint(version, __name__, url_prefix='/v1/api/')
# 创建一个可嵌套蓝图，并将子蓝图注册到该蓝图上
v1_bp.register_blueprint(cmdb_bp)
v1_bp.register_blueprint(user_bp)
