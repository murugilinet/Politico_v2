from flask_restful import reqparse,Resource
from flask import jsonify
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended import get_jwt_identity, jwt_required

parser = reqparse.RequestParser()
parser.add_argument("first_name", type=str, required=True,
                    help="First name field is required")
parser.add_argument("last_name", type=str, required=True,
                    help="Last name field is required")
parser.add_argument("email", type=str, required=True,
                    help="Email field is required")
parser.add_argument("phone_number", type=str, required=True,
                    help="Phone Number field is required")
parser.add_argument("username", type=str, required=True,
                    help="Username field is required")
parser.add_argument("password", type=str, required=True,
                    help="Password field is required")

parser1 = reqparse.RequestParser()
parser1.add_argument("username", type=str, required=True,
                    help="Username is required")
parser1.add_argument("password", type=str, required=True,
                    help="Password field is required")

class Users(Resource):
    def __init__(self):
        self.dt = UserModel()

    def post(self):
        data = parser.parse_args()
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        phone_number = data['phone_number'](self)
        username= data['username']
        password = data['password']
        self.dt.save_user(first_name, last_name, email, phone_number, username, password)

class LogIn(Resource):
    def __init__(self):
        self.dt = UserModel
    
    def post(self):
        data = parser1.parse_args()
        username = data['username']
        password = data['password']
        if not self.dt.get_user_by_username(username):
            return{'No user by username found'}

        login_token = self.dt.user_login(username)
        if login_token:
                return jsonify({
                    'Message': 'Welcome {} to Politico'.format(username),
                    'Token': login_token,
                    'User': self.dt.get_user_by_username(username)
                }, 200