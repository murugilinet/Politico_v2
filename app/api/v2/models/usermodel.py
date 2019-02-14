from app.db_config import Db
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
import re


class UserModel(Db):
    '''This class has queries that access and manipulate data in users table in database'''

    def __init__(self):
        super().__init__()

    def save_user(self, first_name, last_name, email, phone_number, username, password):
        self.cursor.execute(
            "INSERT INTO users(first_name, last_name, email, phonenumber, username, password) VALUES(%s, %s, %s, %s, %s, %s)", 
            (first_name, last_name, email, phone_number, username, password))
        self.connect.commit()

    def get_all(self):
        self.cursor.execute("SELECT * from users")
        user_list = self.cursor.fetchall()
        return user_list

    def get_user_by_username(self, username):
        self.cursor.execute(
            "SELECT * from users WHERE username='{}'".format(username))
        user = self.cursor.fetchall()
        return user

    def get_id(self, username):
        self.cursor.execute(
            "SELECT user_id FROM users WHERE username='{}'".format(username))
        user_id = self.cursor.fetchone()
        return user_id

    def generate_jwt_token(self, username):
        self.user_id = self.get_id(username)
        token = create_access_token(identity=self.user_id)
        return token

    def user_login(self, username):
        token = self.generate_jwt_token(username)
        return token

    def check_exist_email(self, email):
        self.cursor.execute(
            "SELECT * from users WHERE email ='{}'".format(email))
        row = self.cursor.fetchone()
        if row:
            email = row.get('email')
            return email

    def get_password(self, username):
        self.cursor.execute(
            "SELECT  password FROM users WHERE username='{}'".format(username))
        row = self.cursor.fetchone()
        if row:
            password = row.get('password')
            return password

    def check_password(self, username, password):
        pswrd = self.get_password(username)
        return check_password_hash(pswrd, password)

    def confirmpassword(self, password, confirm_password):
        return check_password_hash(password, confirm_password)

    def valid_digits(self, data):
        if data.isdigit():
            return True
        return False

    def valid_input(self, data):
        if data.isalpha():
            return True
        return False

    def valid_email(self, email):
        valid = re.match(
            "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip())
        if valid is None:
            return False
