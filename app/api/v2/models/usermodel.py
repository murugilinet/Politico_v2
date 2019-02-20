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
        row= self.cursor.fetchone()
        if row:
            user_id = row.get('user_id')
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
    
    def promote_user_to_admin(self):
        self.cursor.execute(
           "UPDATE users SET is_admin = 'true'  where username ='admin'")
        self.connect.commit()

    def get_admin_by_id(self,user_id):
        self.cursor.execute(
          "SElECT * from users WHERE user_id = {} and username = 'admin'".format(user_id)
        )
        user = self.cursor.fetchall()
        return user

    def create_admin(self):
        pswrd= generate_password_hash('1234')

        if self.get_user_by_username('admin'):
            return 'Admin already exists!'
        self.save_user('linet', 'murugi','amanadmin@gmail.com', '0720243803','admin', pswrd)
        self.promote_user_to_admin()

    def iamadmin(self, user_id):
        self.cursor.execute(
            "SELECT * from users WHERE user_id = {} and is_admin = 'true'".format(user_id)
        )
        user = self.cursor.fetchall()
        self.promote_user_to_admin()
        return user

    def valid_digits(self, data):
        if data.isdigit():
            return True
        return False

    def valid_input(self, data):
        if data.isalpha():
            return True
        return False
    
    def find_by_id(self,user_id):     
        self.cursor.execute("SELECT * from users WHERE user_id = {}".format(user_id))
        user = self.cursor.fetchall()
        return user

    def valid_email(self, email):
        valid = re.match(
          "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email.strip())
        if valid is None:
            return False

