from dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Director).get(uid)

    def get_all(self, filters):
        page = filters.get('page')
        if page is not None:
            return self.session.query(Director).paginate(int(page),
                                                         per_page=12).items

        return self.session.query(Director).all()

    def create(self, director_d):
        new_director = Director(**director_d)

        self.session.add(new_director)
        self.session.commit()
        return new_director

    def update(self, director_d):
        director = self.get_one(director_d.get("id"))

        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()

    def delete(self, uid):
        director = self.get_one(uid)
        self.session.delete(director)
        self.session.commit()
