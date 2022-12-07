from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO

from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService
from service.auth import AuthService

from setup_db import db

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)

user_dao = UserDAO(session=db.session)
user_service = UserService(dao=user_dao)

auth_service = AuthService(user_service=user_service)
