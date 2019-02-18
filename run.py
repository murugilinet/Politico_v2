import os
from app import create_app
from flask import Flask,current_app
from app.db_config import Db
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended.exceptions import NoAuthorizationError

app = create_app(os.getenv('APP_SETTINGS'))

with app.app_context():
    Db().init_app(app)
    Db().create_tables()
    UserModel().create_admin()

if __name__ == '__main__':
    app.run(debug=True)