from flask import Flask,request,make_response,jsonify
from flask_restful import Resource,reqparse
from app.api.v2.models.officemodel import OfficeModel
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended import get_jwt_identity, jwt_required

parser3 = reqparse.RequestParser()
parser3.add_argument(
    "name",type = str,required = True,help = "Name field is required"
)
parser3.add_argument(
    "age",type = str,required =True,help = "age field required"
)
parser3.add_argument(
    "office_type",type = str,required =True,help = "office_type field required"
)

parser3.add_argument(
    "education",type = str,required =True,help = "education field required"
)
class Offices(Resource):
    #This class and method creates endpoints that allow  users to get all offices created
    def __init__(self):
         self.dt = OfficeModel()
    
    @jwt_required
    def get(self):
       
        if self.dt.get_all() == []:    
            return make_response(jsonify({
                    'Message':'Successfully returned',
                    'data': self.dt.get_all
                }),404)
       
        else:
            return make_response(jsonify({
            'Message':'Returned successfully',
            'data':self.dt.get_all()
            }),200)


class Office(Resource):
    #class and methods creates endpoints that allow users to get a single office by the office_id
    def __init__(self):
         self.dt = OfficeModel()
    @jwt_required   
    def get(self, office_id):
        office = self.dt.find_by_id(office_id)
        if not office:
            return make_response(jsonify({
                'Message':'Office not found'
            }),404)
       
        return make_response(jsonify({
            'Message':'The office has been returned successfully returned',
            'data':office
        }),200)

class AdminOffices(Resource):
    #class provides admin functionality of creating an office
    def __init__(self):
        self.dt = OfficeModel()
        self.admin = UserModel()

    @jwt_required
    def post(self):
        data = parser3.parse_args()
        name = data['name']
        age = data['age']
        office_type = data['office_type']
        education = data['education']


        if not self.admin.iamadmin(get_jwt_identity()):
            return make_response(jsonify({
                'Error': 'You are not an admin!'
             }), 403)
        if self.dt.find_by_name(name):
            return make_response(jsonify({ 'Message': 'Office already exists',}),400)            
       
        if self.dt.valid_type(name) == False: 
            return make_response(jsonify({ 'Message': 'Name input required',}),400) 
         
        if self.dt.valid_digits(age) == False: 
            return make_response(jsonify({ 'Message': 'Age input required',}),400)
      
        if self.dt.valid_type(office_type) == False:
            return make_response(jsonify({ 'Message': 'Office input required',}),400)
        
        if self.dt.valid_type(education) == False: 
            return make_response(jsonify({ 'Message': 'Education input required',}),400)
        
        if self.dt.length_long(name) ==False:
            return make_response(jsonify({
                'Message':'Name field too short'
                 }),411)

        self.dt.save_office(name,age,office_type,education)
      
        return make_response(jsonify({
                'Message': 'Successfully saved',
             }),201)

class AdminOffice(Resource):
    #creates an endpoint that allows admin functionality of deleting  single office

    def __init__(self):
        self.dt = OfficeModel()
        self.admin = UserModel()
        
    @jwt_required
    def delete(self, office_id):
        if not self.admin.iamadmin(get_jwt_identity()):
            return make_response(jsonify({
                'Error': 'You are not an admin!'
             }), 403) 
        office = self.dt.find_by_id(office_id)
        if office:
            self.dt.delete_by_id(office_id)
            return make_response(jsonify({
                'Message': 'Office successfully deleted',
            }), 200)

        return make_response(jsonify({
            'Message': 'Office not found',
        }), 404)