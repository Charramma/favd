from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from tools.error_code import APIAuthorizedException, AuthorizedException
import datetime
from authlib.jose import jwt, JoseError


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token, password):
    """验证入口，兼容三种验证方式"""
    if token and password:
        # 如果token和password都有值表示是用户名密码认证
        return True
    elif token and token == 'api':
        pass
        # 如果token为api表示是api的请求
        # return api_authorize()
    elif token:
        # 如果只有token有值表示是token认证
        user_info = verify_token(token)
        g.user = user_info
        return True
    else:
        raise APIAuthorizedException(message="用户认证失败，参数传递不完整")


def create_token(uid):
    """生成token"""
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


