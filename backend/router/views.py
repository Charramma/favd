from flask import Blueprint

bp = Blueprint("bp", __name__, url_prefix='/')


@bp.route('/')
def index():
    return "Hello World"
