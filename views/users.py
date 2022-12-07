import jwt
from flask import request
from flask_restx import Namespace, Resource

from constants import JWT_SECRET, JWT_ALGORITHM
from container import user_service
from dao.models.user import UserSchema
from decorators import auth_required
from utils import compare_password, make_password_hash

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM, ])
        email = user.get("email")

        result = UserSchema().dump(user_service.get_by_email(email))

        return result, 200

    @auth_required
    def patch(self):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        email = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM, ]).get("email")
        user = user_service.get_by_email(email)

        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = user.id
        if "password" not in request_json:
            request_json["password"] = user.password
        if "email" not in request_json:
            request_json["email"] = user.email
        if "name" not in request_json:
            request_json["name"] = user.name
        if "surname" not in request_json:
            request_json["surname"] = user.surname
        if "favorite_genre" not in request_json:
            request_json["favorite_genre"] = user.favorite_genre
        user_service.update(request_json)
        return "", 204


@user_ns.route('/password')
class UpdatePasswordView(Resource):
    @auth_required
    def put(self):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        email = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM, ]).get("email")
        old_password = request.json.get("password_1")
        new_password = request.json.get("password_2")
        user = user_service.get_by_email(email)

        if compare_password(user.password, old_password):
            user.password = make_password_hash(new_password)
            result = UserSchema().dump(user)
            result["password"] = user.password
            user_service.update(result)
        else:
            print("Password not changed")
        return "", 201
