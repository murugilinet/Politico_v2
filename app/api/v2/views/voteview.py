from flask import Flask,make_response,jsonify,request
from flask_restful import Resource,reqparse
from app.api.v2.models.usermodel import UserModel
from app.api.v2.models.officemodel import OfficeModel
from app.api.v2.models.votemodel import VoteModel
from flask import make_response,jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity

parser5 = reqparse.RequestParser()
parser5.add_argument(
    "createdBy",type = str,required = True,help = "CreatedBy field required"
)
parser5.add_argument(
    "candidate",type = str,required = True,help= "Candidate field required"
)
parser5.add_argument(
    "office",type = str,required = True,help= "Office field required"
)


class VoteUser(Resource):
    def __init__(self):
        self.dt = VoteModel()
        self.admin = UserModel()
        self.off = OfficeModel()
  
    @jwt_required
    def post(self):
        data = parser5.parse_args()
        createdBy = data['createdBy']
        candidate = data['candidate']
        office = data['office']

        if not self.admin.find_by_id(createdBy):
            return make_response(jsonify(
                {'Message':'The User does not exist'}),403)
        if not self.admin.find_by_id(candidate):
            return make_response(jsonify(
                {'Message':'The candidate does not exist'}),403)

        if self.admin.valid_digits(createdBy) == False:
            return make_response(jsonify(
                {'Error':'Voter id should be a digit!'}),400)

        if self.admin.valid_digits(office) == False:
            return make_response(jsonify(
                {'Error':'Office id should be a digit!'}),400)

        if not self.off.find_by_id(office):
            return make_response(jsonify(
                {'Message':'The Office does not exist'}),403)

        if self.dt.exist_vote(createdBy):
            return make_response(jsonify(
                {'Message':'You cannot vote twice'}),401)          

        self.dt.save_vote(createdBy,candidate,office)
        return make_response(jsonify(
                {'Message':'You have successfully cast your vote'}),200)
   
    @jwt_required             
    def get(self):

        if self.dt.get_all() == []:
            return make_response(jsonify({
                'Message': 'Successfully returned',
                'data': self.dt.get_all()
            }), 404)

        else:
            return make_response(jsonify({
                'Message': 'Votes returned successfully',
                'data': self.dt.get_all()
            }), 200)


class Results(Resource):
    def __init__(self):
        self.dt = VoteModel()

    @jwt_required
    def get(self,office_id):
        return make_response(jsonify({
                'Message': 'Votes returned successfully',
                'data': self.dt.get_results(office_id)
            }), 200)


