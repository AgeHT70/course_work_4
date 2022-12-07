from flask import Flask
from flask_restx import Api

from setup_db import db
from config import Config

from views.auths import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    register_extension(app)
    return app


def register_extension(app):
    api = Api(app)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    db.init_app(app)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
