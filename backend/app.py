from flask import Flask
import router
import models


def create_app(config=None):
    app = Flask(__name__)

    # config
    app.config.from_object('config.settings')
    app.config.from_object('config.secure')

    # init blueprint
    router.init_app(app)

    # init model
    models.init_app(app)

    return app
