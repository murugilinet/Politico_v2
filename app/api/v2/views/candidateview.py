from flask import Flask,make_response,jsonify,request
from app.api.v2.models.candidatemodel import CandidateModel
from flask_restful import Resource,reqparse
from app.api.v2.models.usermodel import UserModel
from app.api.v2.models.officemodel import OfficeModel
from app.api.v2.models.partymodel import PartyModel
from flask import make_response,jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity

parser4 = reqparse.RequestParser()
parser4.add_argument(
    "office",type = str,required = True,help = "Office field required"
)
parser4.add_argument(
    "party",type = str,required = True,help = "Party field required"
)
parser4.add_argument(
    "candidate",type = str,required = True,help = "Candidate field required"
)
class AdminCandidate(Resource):
    def __init__(self):
        self.dt = CandidateModel()
        self.admin = UserModel()
        self.off = OfficeModel()
        self.par = PartyModel()
   
    @jwt_required
    def post(self,office_id):
        data = parser4.parse_args()
        office = data['office']
        party = data['party']
        candidate = data['candidate']

   
        if not self.admin.iamadmin(get_jwt_identity()):
            return make_response(jsonify(
                {'Error':'You are not an admin!'}),403)
        
        if self.admin.valid_digits(office) == False:
            return make_response(jsonify(
                {'Error':'Office id should be a digit!'}),400)
    
        if self.admin.valid_digits(party) == False:
            return make_response(jsonify(
                {'Error':'Party id should be a digit!'}),400)

        if self.admin.valid_digits(candidate) == False:
            return make_response(jsonify(
                {'Error':'Candidate id should be a digit!'}),400)

        if not self.off.find_by_id(office):
            return make_response(jsonify(
                {'Error':'Office Not Found'}),404)

        if self.dt.exist_candidate(candidate,office):
            return make_response(jsonify(
                {'Error':'Candidate already registered'}),400)

        if not self.par.find_by_id(party):
            return make_response(jsonify(
                {'Error':'Party Not Found'}),404)
            
        if not self.admin.find_by_id(candidate):
            return make_response(jsonify(
                {'Error':'Candidate does not exist'}),404)
        
        self.dt.save_candidate(office,party,candidate)
        return make_response(jsonify(
                {'Message':'You have successfully created a candidate'}),200)

        
