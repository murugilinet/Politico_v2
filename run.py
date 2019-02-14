import os
from app import create_app
from flask import Flask,current_app
from app.db_config import Db

app = create_app(os.getenv('APP_SETTINGS'))

with app.app_context():
    Db().init_app(app)
    Db().create_tables()

if __name__ == '__main__':
    app.run(debug=True)