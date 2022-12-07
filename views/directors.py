from flask import request
from flask_restx import Resource, Namespace

from dao.models.director import DirectorSchema
# from decorators import auth_required, admin_required
from container import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    # @auth_required
    def get(self):
        page = request.args.get('page')
        filters = {"page": page}
        directors = director_service.get_all(filters)
        schema = DirectorSchema(many=True)
        result = schema.dump(directors)
        return result, 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    # @auth_required
    def get(self, uid):
        director = director_service.get_one(uid)
        schema = DirectorSchema()
        result = schema.dump(director)
        return result, 200
