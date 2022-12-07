import calendar
import datetime
import jwt

from constants import JWT_ALGORITHM, JWT_SECRET
from service.user import UserService
from utils import compare_password


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise Exception("user is None")

        if not is_refresh:
            if not compare_password(user.password, password):
                raise Exception()

        data = {
            'email': user.email
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET,
                                  algorithm=JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET,
                                   algorithm=JWT_ALGORITHM)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def verify_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[
            JWT_ALGORITHM, ])
        email = data.get('email')
        user = self.user_service.get_by_email(email)
        if user is None:
            raise Exception()

        return self.generate_token(email, user.password, is_refresh=True)

    def validate_token(self, access_token, refresh_token):
        for token in [access_token, refresh_token]:
            try:
                jwt.decode(jwt=token, key=JWT_SECRET, algorithms=[
                    JWT_ALGORITHM,])
            except Exception as e:
                return False
        return True
