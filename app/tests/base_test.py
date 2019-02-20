import unittest
import json
from app.db_config import Db
from app import create_app
from flask import make_response,jsonify
from app.api.v2.models.usermodel import UserModel

app = create_app('testing')
class BaseTest(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        Db().init_app(app)
        Db().create_tables()
        UserModel().create_admin()

        self.test_user = {
            'first_name':'Linet',
            'last_name':'Murugi',
            'email':'murugi@gmail.com',
            'phone_number':'0702529853',
            'username':'koko',
            'password':'mypassword',
            'confirm_password':'mypassword'            
        }

        self.test_user1 = {
            'first_name':'Linet',
            'last_name':'Murugi',
            'email':'murugilinet@gmail.com',
            'phone_number':'0720243803',
            'username':'koko',
            'password':'password',
            'confirm_password':'password'
        }

        self.test_user2 = {
            'first_name':'Linet',
            'last_name':'Murugi',
            'email':'murugi@gmail.com',
            'phone_number':'0727838031',
            'username':'Nimo',
            'password':'pass',
            'confirm_password':'pass'
        }

        self.test_user3= {
            'first_name':'Linet',
            'last_name':'Murugi',
            'email':'murugilinetgmail.com',
            'phone_number':'072783803',
            'username':'Don',
            'password':'pass',
            'confirm_password':'pass'
        }
        self.test_user4= {
            'first_name':'Linet',
            'last_name':'Murugi',
            'email':'murugilinetgmail.com',
            'phone_number':'072783803',
            'username':'bobo',
            'password':'123456',
            'confirm_password':'pass'
        }
    
       
        self.test_missing_name1 = {
            'first_name':'',
            'last_name':'Murugi',
            'email':'murugilinet@gmail.com',
            'phone_number':'0720243803',
            'username':'Nimo',
            'password':'password',
            'confirm_password':'password'
        }
        self.test_email_invalid = {
            'first_name':'Linet',
            'last_name':'Murugi',
            'email':'murugilinetgmail.com',
            'phone_number':'0720243803',
            'username':'pumpy',
            'password':'password',
            'confirm_password':'password'
        }
        self.test_password_different = {
            'first_name':'Linet',
            'last_name':'Murugi',
            'email':'njaguara@gmail.com',
            'phone_number':'0720243803',
            'username':'Mimo',
            'password':'password',
            'confirm_password':'passwor'
        }
        self.test_login1 ={
             'username':'buki',
             'password':'mypassword'}

    
    
        self.userlogin = {'username': self.test_user['username'],
                          'password': self.test_user['password']}

        self.admin = {'username': 'admin',
                      'password': '1234'}

        # self.loginnormaluser = {'username': self.test_user5['username'],
        #                         'password': self.test_user5['password']}
        self.test_office = {
            'name':'Governor',
            'age':'35',
            'office_type':'state',
            'education':'Olevel'
             }
        self.test_office_missing_name = {
            'name':'',
            'age':'35',
            'office_type':'federal',
            'education':'Olevel'
        }
        self.test_office_short_name = {
            'name':'Pre',
            'age':'35',
            'office_type':'state',
            'education':'Olevel'
        }
        self.test_office_missing_office_type = {
            'name':'President',
            'age':'35',
            'office_type':'',
            'education':'O-level'
        }
        self.test_office2 = {
            'name':'Senator',
            'age':'21',
            'office_type':'juja',
            'education':'Degree'
        }
        self.test_party1 = {
            'name':'Harambee',
            'abbreviations':'JGP',
            'chairperson':'Suleiman',
            'members':'18',
            'address':'254nai',
            'logoUrl':'logo'
            }
        self.test_party2 = {
            'name':'Harambee',
            'abbreviations':'JGP',
            'chairperson':'Suleiman',
            'members':'18',
            'address':'254nai',
            'logoUrl':'logo'
            }
        self.test_party_missing_name = {
            'name':'',
            'abbreviations':'AFC',
            'chairperson':'Abdul',
            'members':'56',
            'address':'255emb',
            'logoUrl':'logoo'
        }
        self.test_party_short_name = {
            'name':'Afri',
            'abbreviations':'AFA',
            'chairperson':'Abdulkim',
            'members':'54',
            'address':'254nai',
            'logoUrl':'logo'
            }
        self.test_party4= {
            'name':'knyan',
            'abbreviations':'AFAKAR',
            'chairperson':'Abdi',
            'members':'54',
            'address':'25naks',
            'logoUrl':'logo'
            }
        self.test_party_missing_logo = {
            'name':'mumbi',
            'abbreviations':'AFC',
            'chairperson':'Abdul',
            'members':'56',
            'address':'25nanyu',
            'logoUrl':' '
        }


    def registration(self):
        response = self.app.post('/api/v2/auth/signup',
                                 json=self.test_user,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def unmatching_pswrd_registration(self):
        response = self.app.post('/api/v2/auth/signup',
                                 json=self.test_password_different,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def existing_username_registration(self):
        response = self.app.post('/api/v2/auth/signup',
                                 json=self.test_user1,
                                 headers={'content-type': 'application/json'}
                                 )
        return response
 
    def existing_email_registration(self):
        response = self.app.post('/api/v2/auth/signup',
                                 json=self.test_user2,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def invalid_email_registration(self):
        response = self.app.post('/api/v2/auth/signup',
                                 json=self.test_user3,
                                 headers={'content-type': 'application/json'}
                                 )
        return response
    
    def missing_first_name(self):
        response = self.app.post('/api/v2/auth/signup',
                                json = self.test_missing_name1,
                                headers = {'content-type': 'application/json'} )
        return response
    
    def login(self):
        response = self.app.post('/api/v2/auth/login',
                                json = self.userlogin,
                                headers={'content-type':'application/json'} )
        return response

    def login_unregistered(self):
        response = self.app.post('/api/v2/auth/login',
                                json = self.test_login1,
                                headers={'content-type':'application/json'} )
        return response

    def loginadmin(self):
        response = self.app.post('/api/v2/auth/login',
                                 json=self.admin,
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    # def err_pswrd_login(self):
    #     response = self.app.post('/api/v2/auth/login',
    #                             json = self.test_login2,
    #                             headers={'content-type':'application/json'} )
        # return response

    def admintoken(self):
        self.resp = self.loginadmin()
        self.tok = json.loads(self.resp.data)
        # print(self.tok)
        self.token = self.tok['Token']
        return self.token

    def usertoken(self):
        self.registration()
        self.resp = self.login()
        self.tok = json.loads(self.resp.data)
        self.token = self.tok['Token']
        return self.token

    def register_office(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/offices',
                                 json=self.test_office,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def short_name_registration(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/offices',
                                 json=self.test_office_short_name,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def missing_name_registration(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/offices',
                                 json=self.test_office_missing_name,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def missing_type_registration(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/offices',
                                 json=self.test_office_missing_office_type,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def invalid_type_registration(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/offices',
                                 json=self.test_office2,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def delete_by_id(self):
        token = self.admintoken()
        response = self.app.delete('/api/v2/offices/1',
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def get_by_id(self):
        token = self.usertoken()
        response = self.app.get('/api/v2/offices/1',
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def get_all(self):
        token = self.usertoken()
        response = self.app.get('/api/v2/offices',
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def register_party(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/parties',
                                 json=self.test_party1,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def existing_party(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/parties',
                                 json=self.test_party2,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def register_missing_partyname(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/parties',
                                 json=self.test_party_missing_name,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def register_short_partyname(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/parties',
                                 json=self.test_party_short_name,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def register_long_abbreviations(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/parties',
                                 json=self.test_party4,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def register_missing_logo(self):
        token = self.admintoken()
        response = self.app.post('/api/v2/parties',
                                 json=self.test_party_missing_logo,
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def get_party_by_id(self):
        token = self.usertoken()
        response = self.app.get('/api/v2/parties/1',
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def delete_party_by_id(self):
        token = self.admintoken()
        response = self.app.delete('/api/v2/parties/1',
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response

    def get_all_parties(self):
        token = self.usertoken()
        response = self.app.get('/api/v2/parties',
                                 headers={'Authorization': 'Bearer {}'.format(token),
                                          'content-type': 'application/json'}
                                 )
        return response
    def tearDown(self):
        Db().destroy_tables()
        self.app_context.pop()
        