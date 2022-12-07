from flask import request
from flask_restx import Resource, Namespace

from dao.models.genre import GenreSchema
# from decorators import auth_required, admin_required
from container import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresViews(Resource):
    # @auth_required
    def get(self):
        page = request.args.get('page')
        filters = {"page": int(page)}
        genres = genre_service.get_all(filters)
        schema = GenreSchema(many=True)
        result = schema.dump(genres)
        return result, 200


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    # @auth_required
    def get(self, uid):
        genre = genre_service.get_one(uid)
        schema = GenreSchema()
        result = schema.dump(genre)
        return result, 200
