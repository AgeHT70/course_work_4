from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self, filters):
        return self.dao.get_all(filters)

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, genre_d):
        self.dao.update(genre_d)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)
