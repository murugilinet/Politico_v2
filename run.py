import os
from app import create_app
from flask import Flask,current_app,jsonify,request
from app.db_config import Db
from app.api.v2.models.usermodel import UserModel
from flask_jwt_extended.exceptions import NoAuthorizationError

app = create_app(os.getenv('APP_SETTINGS'))

with app.app_context():
    Db().init_app(app)
    Db().create_tables()
    UserModel().create_admin()




@app.errorhandler(404)
def invalid_endpoint(error=None):
    """Handle wrong endpoints url"""
    return jsonify({
        'Message': '{} is not a valid url'.format(request.url)
    }), 404


@app.errorhandler(405)
def wrong_method(error=None):
    """Handle wrong methods for an endpoint """
    request_method = request.method
    return jsonify({
        'Message': 'The {} method is not allowed for this endpoint'
        .format(request_method)}), 405


@app.errorhandler(400)
def wrong_request(error=None):
    """Handle wrong forms of requests for an endpoint """
    return jsonify({
        'Message': 'This endpoint supports JSON requests only.'}), 400


@app.errorhandler(500)
def server_error(error=None):
    """Handle internal server error for an endpoint """
    return jsonify({
        'Message': 'Verify if the request causes a server error'}), 500

@app.errorhandler(NoAuthorizationError)
def no_authorization(error=None):
        """Handle no authorization error"""
        return jsonify({
                'Message' : 'You are not logged in!'
}), 

if __name__ == '__main__':
    app.run(debug=True)