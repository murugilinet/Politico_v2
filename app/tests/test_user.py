import json
from app.tests.base_test import BaseTest


class UsersTest(BaseTest):
    def test_create_user(self):
        response = self.registration()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'User saved')
        self.assertEqual(response.status_code,200)
    

    def test_missing_firstname(self):
         response = self.missing_first_name()
         result = json.loads(response.data)
         self.assertEqual(result['Error'],'valid first name required')
         self.assertEqual(response.status_code,422)  

    def test_invalid_email(self):
         response = self.invalid_email_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Error'],'valid email required')
         self.assertEqual(response.status_code,422)

    def test_unmatching_passwords(self):    
         response = self.unmatching_pswrd_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Error'],'passwords do not match')
         self.assertEqual(response.status_code,401)

    def test_existing_email(self):    
         self.registration()
         response = self.existing_email_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Error'],'email already exist')
         self.assertEqual(response.status_code,401)
    
    def test_existing_username(self):    
         self.registration()
         response = self.existing_username_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Error'],'username already exist')
         self.assertEqual(response.status_code,401)


    def test_login_user(self):
        self.registration()
        response = self.login()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Welcome koko to Politico')
        self.assertEqual(response.status_code,200)
 
    # def test_wrong_password(self):    
    #      self.registration()
    #      response = self.err_pswrd_login()
    #      result = json.loads(response.data)
    #      self.assertEqual(result['Error'],'Wrong Password')
    #      self.assertEqual(response.status_code,404)

    def test_unregistered_user(self): 
        response = self.login_unregistered()
        result = json.loads(response.data)
        self.assertEqual(result['Error'],'No user by this username found')
        self.assertEqual(response.status_code,404)