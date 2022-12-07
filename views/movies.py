from flask import request, abort
from flask_restx import Resource, Namespace

from dao.models.movie import MovieSchema
# from decorators import auth_required, admin_required
from container import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    # @auth_required
    def get(self):
        page = request.args.get('page')
        status = request.args.get('status')
        filters = {
            "page": page,
            "status": status
        }
        all_movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    @movie_ns.route('/<int:uid>')
    class MovieView(Resource):
        # @auth_required
        def get(self, uid):
            movie = movie_service.get_one(uid)
            if movie is None:
                abort(404)
            result = MovieSchema().dump(movie)
            return result, 200
