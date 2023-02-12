from .views import bp
from .v1 import v1_bp


def init_app(app):
    app.register_blueprint(bp)
    app.register_blueprint(v1_bp)
