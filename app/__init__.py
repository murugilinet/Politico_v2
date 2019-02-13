from flask import Flask, Blueprint, jsonify, request
from instance.config import app_config

# from .api import version_one as v1 


def create_app(config_name='testing'):
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config['testing'])
    app.config.from_pyfile('config.py')
    #app.register_blueprint(v1)
    return app