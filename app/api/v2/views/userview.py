from flask_restful import reqparse,Resource
from flask import jsonify,make_response
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash

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
parser.add_argument("confirm_password", type=str, required=True,
                    help="confirm your password")

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
        phone_number = data['phone_number']
        username= data['username']
        password = generate_password_hash(data['password'])
        confirm_password = data['confirm_password']

        if self.dt.valid_input(first_name)== False:
            return make_response(jsonify({'Error':'valid first name required'}),422)

        if self.dt.valid_input(last_name)== False:
            return make_response(jsonify({'Error':'valid last name required'}),422)

        if self.dt.valid_email(email)== False:
            return make_response(jsonify({'Error' :'valid email required'}),422)

        if self.dt.valid_digits(phone_number)== False:
            return make_response(jsonify({'Error':'valid number required'}),422)

        if self.dt.get_user_by_username(username):
            return make_response(jsonify({'Error':'username already exist'}),401)

        if self.dt.check_exist_email(email):
            return make_response(jsonify({'Error':'email already exist'}),401)

        if not self.dt.confirmpassword(password, confirm_password):
            return make_response(jsonify({'Error':'passwords do not match'}),401)
       
        self.dt.save_user(first_name, last_name, email, phone_number, username, password)
        return make_response(jsonify({'Message': 'You have successfully created an account'}),200)


 
class LogIn(Resource):
    def __init__(self):
        self.dt = UserModel()
    
    def post(self):
        data = parser1.parse_args()
        username = data['username']
        password = data['password']
        if not self.dt.get_user_by_username(username):
             return make_response(jsonify({'Error':'No user by this username found'}),404)
        
        if not self.dt.check_password(username, password):
             return make_response(jsonify({'Error':'Wrong Password'}),404)
        login_token = self.dt.user_login(username)
       
        if login_token:
                return make_response(jsonify({
                     'Message': 'Welcome {} to Politico'.format(username),
                    'Token': login_token,
                   'User': self.dt.get_user_by_username(username)
                }), 200)