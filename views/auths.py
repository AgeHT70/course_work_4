from flask import request, abort
from flask_restx import Resource, Namespace

from container import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        request_json = request.json
        email = request_json.get('email')
        password = request_json.get('password')
        if None in [email, password]:
            abort(400)
        user_service.create(request_json)
        return '', 201


@auth_ns.route('/login')
class AuthLoginView(Resource):
    def post(self):
        request_json = request.json
        email = request_json.get('email')
        password = request_json.get('password')
        if None in [email, password]:
            abort(400)
        tokens = auth_service.generate_token(email, password)
        return tokens, 201

    def put(self):
        request_json = request.json
        access_token = request_json.get('access_token')
        refresh_token = request_json.get('refresh_token')
        if None in [access_token, refresh_token]:
            abort(400)
        if not auth_service.validate_token(access_token, refresh_token):
            return "Invalid token", 400
        tokens = auth_service.verify_token(refresh_token)

        return tokens, 201
