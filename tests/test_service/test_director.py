import pytest

from service.director import DirectorService


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None
        assert director.name == 'Director 1'

    def test_get_all(self):
        filter = {"page": 1}
        directors = self.director_service.get_all(filter)
        assert directors is not None
        assert len(directors) > 0

    def test_create(self):
        director_dict = {"name": "Director 4", }
        director = self.director_service.create(director_dict)
        assert director is not None
        assert director.id is not None

    def test_update(self):
        director_dict = {"id": 3, "name": "new Director 3", }
        assert self.director_service.update(director_dict)

    def test_delete(self):
        assert self.director_service.delete(1) is None
