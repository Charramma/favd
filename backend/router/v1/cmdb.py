from libs.nestable_blueprint import NestableBlueprint
from flask_restful import Api, Resource
from models.cmdb import Server
from serializer.cmdb_serializer import server_schema, servers_schema
from libs.authorize import api_authorize
from libs.response import generate_response
from libs.handler import default_error_handler
from libs.authorize import auth
from libs.parse import servers_parse

cmdb_bp = NestableBlueprint(f'cmdb_v1', __name__, url_prefix='cmdb')
api = Api(cmdb_bp)

# 指定当出现异常时，所调用的处理方法
api.handle_error = default_error_handler


class ServersView(Resource):
    @auth.login_required
    def get(self):
        # api_authorize()     # 进行api认证
        servers = Server.query.all()
        # return generate_response(data=servers_schema.dump(servers))
        return generate_response(data=servers_parse(servers))

    def post(self):
        api_authorize()


api.add_resource(ServersView, '/servers/')
