from app.db_config import Db
from flask_jwt_extended import create_access_token

class UserModel(Db):
    '''This class has queries that access and manipulate data in users table in database'''

    def __init__(self):
     super().__init__()

    def save_user(self,first_name,last_name,email,phone_number,username,password):
        
        self.cursor.execute(
            "INSERT INTO users(first_name,last_name,email,phone_number username,password)VALUES (%s,%s,%s,%s,%s,%s)",
            (first_name,last_name,email,phone_number,username,password))
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
        user_id = self.cursor.fetchone
        return user_id

    def generate_jwt_token(self, username):
        self.user_id = self.get_id(username)
        token = create_access_token(identity=self.user_id)
        return token
    
    def user_login(self, username):
        token = self.generate_jwt_token(username)
        return token