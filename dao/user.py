from dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email ==
                                               email).first()

    def create(self, user_d):
        new_user = User(**user_d)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))

        user.email = user_d.get("email")
        user.password = user_d.get("password")
        user.name = user_d.get("name")
        user.surname = user_d.get("surname")
        if user_d.get("favorite_genre") is not None:
            user.favorite_genre = int(user_d.get("favorite_genre"))

        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()