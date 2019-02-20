from flask import Flask, request, make_response, jsonify
from flask_restful import Resource, reqparse
from app.api.v2.models.partymodel import PartyModel
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended import jwt_required,get_jwt_identity

parser2 = reqparse.RequestParser()
parser2.add_argument(
    "name", type=str, required=True, help="Name field is required"
)
parser2.add_argument(
    "abbreviations", type=str, required=True, help="Abbreviation field required"
)
parser2.add_argument(
    "chairperson", type=str, required=True, help="Chairperson field required"
)

parser2.add_argument(
    "members", type=str, required=True, help="Members field required"
)
parser2.add_argument(
    "address", type=str, required=True, help="Address field required"
)
parser2.add_argument(
    "logoUrl", type=str, required=True, help="Logo field required"
)


class Parties(Resource):
    # This class and methods creates endpoints that allow users to view all parties
    def __init__(self):
        self.dt = PartyModel()
    

    def get(self):

        if self.dt.get_all() == []:
            return make_response(jsonify({
                'Message': 'Parties successfully returned but no party has been created yet',
                'data': self.dt.get_all()
            }), 404)

        else:
            return make_response(jsonify({
                'Message': 'Parties successfully returned',
                'data': self.dt.get_all()
            }), 200)


class Party(Resource):
    # class and methods creates endpoints that allow users to view a single party using the party id
    def __init__(self):
        self.dt = PartyModel()
    @jwt_required
    def get(self, party_id):
        party = self.dt.find_by_id(party_id)
        if not party:
            return make_response(jsonify({
                'Message': 'Party not found'
            }), 404)

        return make_response(jsonify({
            'Message': 'The party has been returned successfully',
            'data': party
        }), 200)


class AdminParties(Resource):
    #creates an endpoint that allows the admin to create a party
    def __init__(self):
        self.dt = PartyModel()
        self.admin = UserModel()
    @jwt_required
    def post(self):
        data = parser2.parse_args()
        name = data['name']
        abbreviations = data['abbreviations']
        chairperson =data['chairperson']
        members = data['members']
        address = data['address']
        logoUrl =data['logoUrl']

        if not self.admin.iamadmin(get_jwt_identity()):
            return make_response(jsonify({'Error': 'You are not an admin!'}), 403)

        if self.dt.find_by_name(name):
            return make_response(jsonify({'Message': 'Party already exists'}), 401)

        if self.dt.valid_type(name) == False:
            return make_response(jsonify({ 'Message': 'Name input required'}), 400)

        if self.dt.valid_type(abbreviations) == False:
            return make_response(jsonify({ 'Message': 'abbreviations input required'}), 400)

        if self.dt.valid_type(chairperson) == False:
            return make_response(jsonify({ 'Message': 'chairperson input required'}), 400)

        if self.dt.valid_digits(members) == False:
            return make_response(jsonify({ 'Message': 'members input required'}), 400)

        if self.dt.valid(address) == False:
            return make_response(jsonify({ 'Message': 'address input required'}), 400)

        if self.dt.valid_type(logoUrl) == False:
            return make_response(jsonify({ 'Message': 'logo input required'}), 400)

        if self.dt.length_long(name) == False:
            return make_response(jsonify({'Message': 'Name field too short'}), 411)

        if self.dt.length_short(abbreviations) == False:
            return make_response(jsonify({'Message': 'abbreviations too long'}), 411)

        self.dt.save_party(name,abbreviations,chairperson,members,address,logoUrl)
        return make_response(jsonify({'Message': 'You have successfully created a party'}), 201)


class AdminParty(Resource):
    #creates endpoints that allow adminuser to delete and edit a party using the party id
    def __init__(self):
        self.dt = PartyModel()
        self.admin = UserModel()

    @jwt_required
    def delete(self, party_id):
        if not self.admin.iamadmin(get_jwt_identity()):
            return make_response(jsonify({'Error': 'You are not an admin!'}), 403)
        party = self.dt.find_by_id(party_id)
        if party:
            self.dt.delete_by_id(party_id)
            return make_response(jsonify({
                'Message': 'You have successfully deleted the party',
            }), 200)

        return make_response(jsonify({
            'Message': 'Party not found',
        }), 404)

    @jwt_required
    def patch(self, party_id):
        if not self.admin.iamadmin(get_jwt_identity()):
            return make_response(jsonify({'Error': 'You are not an admin!'}), 403)
        data = parser2.parse_args()
        name = data['name']
        party = self.dt.find_by_id(party_id)
        if party:
            self.dt.updatename(party_id, name)
            return make_response(jsonify({
                'Message': 'You have successfully updated the party' 
            }), 200)

        return make_response(jsonify({
            'Message': 'Party not found'
        }), 404)