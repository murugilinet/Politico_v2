from flask import Blueprint 
from flask_restful import Api,Resource
from app.api.v2.views.officeview import Offices,Office,AdminOffices,AdminOffice
from app.api.v2.views.partyview  import Parties,Party,AdminParties,AdminParty
from app.api.v2.views.userview  import Users,LogIn

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two)

api.add_resource (Offices, '/offices')
api.add_resource (AdminOffices, '/offices')
api.add_resource (Office, '/offices/<int:office_id>')
api.add_resource (AdminOffice, '/offices/<int:office_id>')
api.add_resource (Parties, '/parties')
api.add_resource (AdminParties, '/parties')
api.add_resource (Party, '/parties/<int:party_id>')
api.add_resource (AdminParty, '/parties/<int:party_id>')
api.add_resource (Users, '/auth/signup')
api.add_resource (LogIn, '/auth/login')

