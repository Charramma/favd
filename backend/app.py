from flask import Flask
import router
import models
import serializer
from flask_cors import CORS


def create_app(config=None):
    app = Flask(__name__)

    # 配置跨域资源共享
    cors = CORS(app, resource={'*': {'origins': '*'}})

    # config
    app.config.from_object('config.settings')
    app.config.from_object('config.secure')

    # init blueprint
    router.init_app(app)

    # init model
    models.init_app(app)

    serializer.init_app(app)

    return app
