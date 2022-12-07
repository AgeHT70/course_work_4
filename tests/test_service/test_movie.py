import pytest

from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == 'Movie 1'

    def test_get_all(self):
        filter = {"status": "new"}
        movies = self.movie_service.get_all(filter)
        assert movies is not None
        assert len(movies) > 0

    def test_create(self):
        movie_dict = {
            "title": "Movie 4",
            "description": "Description 4",
            "trailer": "Trailer 4",
            "year": 2010,
            "rating": 8.0,
            "genre_id": 1,
            "director_id": 1
        }
        movie = self.movie_service.create(movie_dict)
        assert movie is not None
        assert movie.id is not None

    def test_update(self):
        movie_dict = {
            "id": 1,
            "title": "new Movie",
            "description": "new Description",
            "trailer": "Trailer 4",
            "year": 2010,
            "rating": 8.0,
            "genre_id": 1,
            "director_id": 1
        }
        assert self.movie_service.update(movie_dict)

    def test_delete(self):
        assert self.movie_service.delete(1) is None