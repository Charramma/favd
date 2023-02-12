from hashlib import md5
from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from libs.error_code import APIAuthorizedException, AuthorizedException, PermissionDeny
from models.user import APIToken, UserProfile
from authlib.jose import jwt, JoseError
from libs.response import generate_response
import datetime

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token, password):
    """验证入口，兼容三种验证方式"""
    if token and password:
        # 如果token和password都有值表示是用户名密码认证
        return True
    elif token and token == 'api':
        # 如果token为api表示是api的请求
        return api_authorize()
    elif token:
        # 如果只有token有值表示是token认证
        user_info = verify_token(token)
        g.user = user_info
        return True
    else:
        raise APIAuthorizedException(message="用户认证失败，参数传递不完整")


def create_token(uid):
    # 签名算法
    header = {'alg': 'HS256'}
    payload = {
        'uid': uid,
        'exp': int(
            (datetime.datetime.utcnow() + datetime.timedelta(seconds=current_app.config["EXPIRES_IN"])).timestamp()),
    }
    token = jwt.encode(header, payload, key=current_app.config["SECRET_KEY"]).decode('ascii')
    return token


def verify_token(token):
    """验证token是否合法"""
    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"])
    except JoseError as e:
        raise AuthorizedException(message='无效的token')
    return payload


def api_authorize():
    # 获取查询参数 => get请求 => url上的参数 request.args
    # request => 当前请求（线程隔离）
    params = request.args
    # 如果没有值，给一个空串
    appid = params.get('appid', "")
    salt = params.get('salt', "")
    sign = params.get('sign', "")

    # 从数据库中获取对应appid的token，从中获取secretkey
    api_token = APIToken.query.filter_by(api_token_appid=appid).first()
    if not api_token:
        raise APIAuthorizedException(message="认证失败！没有查找到api_token")
    else:
        # 如果获取到token, 检查是否有权限
        # has_permission(api_token, url=request.path, method=request.method)
        pass

    # 生成对照sign
    user_appid = api_token.api_token_appid
    user_secretkey = api_token.api_token_secretkey
    user_sign = str(user_appid) + salt + user_secretkey
    m1 = md5()
    m1.update(user_sign.encode(encoding='utf8'))
    user_sign = m1.hexdigest()
    # 如果验证失败，抛出异常
    if sign != user_sign:
        raise APIAuthorizedException()
    else:
        return True


def permission_required(func):
    def _dec(*args, **kwargs):
        # 获取当前用户
        user = UserProfile.query.get(g.user["uid"])
        # 判断是否有权限
        has_permission(user.role, url=request.path, method=request.method)
        return func(*args, **kwargs)

    return _dec


def has_permission(api_token, url, method):
    """权限该api是否有指定url和指定方法的权限"""
    # 从服务端查找appid及对应的秘钥
    # GET/v1/api/cmdb/servers/
    mypermission = method + url
    if api_token:
        all_permissions = [permission.method_type.name + permission.url for permission in
                           api_token.permissions]
        if mypermission not in all_permissions:
            raise PermissionDeny(message="没有当前接口的权限")
    else:
        raise PermissionDeny(message="获取用户信息失败！")
    return True
