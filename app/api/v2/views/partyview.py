from flask import Flask,request,make_response,jsonify
from flask_restful import Resource,reqparse
from app.api.v2.models.partymodel import PartyModel


parser2 = reqparse.RequestParser()
parser2.add_argument(
    "name",type = str,required = True,help = "Name field is required"
)
parser2.add_argument(
    "abbreviations",type = str,required =True,help = "abbreviation field required"
)
parser2.add_argument(
    "chairperson",type = str,required =True,help = "chairperson field required"
)

parser2.add_argument(
    "members",type = str,required =True,help = "members field required"
    )
parser2.add_argument(
    "address",type = str,required =True,help = "address field required"
    )
parser2.add_argument(
    "logoUrl",type = str,required =True,help = "logo field required"
    )

class Parties(Resource):
    #This class and methods creates endpoints that work on several parties
    def __init__(self):
        self.dt = PartyModel()

    def post(self):
        data = parser2.parse_args()

        party = {
            'name': data['name'],
            'abbreviations':data['abbreviations'],
            'chairperson':data['chairperson'],
            'members':data['members'],
            'address':data['address'],
            'logoUrl':data['logoUrl'],
               } 


        response = make_response(jsonify({
            'Message':'Correct input required',
            }),400)
      
        if self.dt.find_by_name ==  False:
            return make_response(jsonify({
                'Message': 'Party already exists'
             }),401)
      
        if self.dt.valid_type(data['name']) ==  False:
            return response
       
        if self.dt.valid_type(data['abbreviations']) ==  False:
            return response
       
        if self.dt.valid_type(data['chairperson']) ==  False:
            return response
       
        if self.dt.valid_digits(data['members']) == False:
            return response
        
        if self.dt.valid(data['address']) == False:
            return response
      
        if self.dt.valid_type(data['logoUrl']) == False:
            return response
       
        elif self.dt.length_long(data['name']) == False:
            return make_response(jsonify({
                'Message':'Name field too short'
            }),411)
      
        elif self.dt.length_short(data['abbreviations']) ==False:
            return make_response(jsonify({
                'Message':'abbreviations too long'
             }),411)
        self.dt.save_party
      
        return make_response(jsonify({
                'Message': 'Successfully saved',
                'data':party
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


class Party(Resource):
    #class and methods creates endpoints that apply to a single party only
    def __init__(self):
         self.dt = PartyModel()
       
    def get(self, party_id):
        party = self.dt.find_by_id(party_id)
        if not party:
            return make_response(jsonify({
                'Message':'Party not found'
            }),404)
       
        return make_response(jsonify({
            'Message':'The party has been returned successfully',
            'data':party
        }),200)

    def delete(self, party_id):
        party = self.dt.find_by_id(party_id)
        if party:
            self.dt.delete_by_id(party_id)
            return make_response(jsonify({
                'Message':'Party successfully deleted',
                'data':party
            }),200)
       
        return make_response(jsonify({
            'Message':'Party not found',
           }),404)

    def patch(self,party_id):
        data = parser2.parse_args()
        name = data ['name']
        party = self.dt.find_by_id(party_id)
        if party:
              self.dt.updatename(party_id,name)
              return make_response(jsonify({
                'Message':'party successfully updated',
                'data':party
            }),200)
       
        return make_response(jsonify({
            'Message':'Party not found'
            }),404)
 