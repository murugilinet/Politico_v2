from flask import Flask,request,make_response,jsonify
from flask_restful import Resource,reqparse
from app.api.v2.models.officemodel import OfficeModel


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
    #This class and methods creates endpoints that work on several offices
    def __init__(self):
        self.dt = OfficeModel()

    def post(self):
        data = parser3.parse_args()

        office = {
            'name': data['name'],
            'age':data['age'],
            'office_type':data['office_type'],
            'education':data['education'],
               } 


        response = make_response(jsonify({
            'Message': 'Correct input required',
        }),400) 
       
        if self.dt.valid_type(data['name']) == False: 
            return response
         
        if self.dt.valid_digits(data['age']) == False: 
            return response
      
        if self.dt.valid_type(data['office_type']) == False:
            return response
        
        if self.dt.valid_type(data['education']) == False: 
            return response
        
        elif self.dt.length_long(data['name']) ==False:
            return make_response(jsonify({
                'Message':'Name field too short'
                 }),411)

        self.dt.save_office
      
        return make_response(jsonify({
                'Message': 'Successfully saved',
                'data':office
             }),201)
    
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
    #class and methods creates endpoints that apply to a single party only
    def __init__(self):
         self.dt = OfficeModel()
       
    def get(self, office_id):
        office = self.dt.find_by_id(office_id)
        if not office:
            return make_response(jsonify({
                'Message':'Office not found'
            }),404)
       
        return make_response(jsonify({
            'Message':'The office has been returned successfully',
            'data':office
        }),200)

    def delete(self, office_id):
        party = self.dt.find_by_id(office_id)
        if party:
            self.dt.delete_by_id(office_id)
            return make_response(jsonify({
                'Message':'Office successfully deleted',
                'data':party
            }),200)
       
        return make_response(jsonify({
            'Message':'Office not found',
           }),404)
 