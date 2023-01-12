from  .extension import db
from flask_migrate import Migrate


def init_app(app):
    migrate = Migrate(app, db)
    db.init_app(app)
