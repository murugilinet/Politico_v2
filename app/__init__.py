from flask import Flask, Blueprint, jsonify, request, current_app
from instance.config import Config, app_config
from flask_jwt_extended import JWTManager
from .api.v2.views import version_two as v2 


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(v2)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    JWTManager(app)
    
    return app