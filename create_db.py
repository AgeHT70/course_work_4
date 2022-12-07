from contextlib import suppress

from sqlalchemy.exc import IntegrityError

from app import create_app
from config import Config
from dao.models.director import Director
from dao.models.genre import Genre
from dao.models.movie import Movie
from setup_db import db

import json


def read_json(filename: str, encoding: str = "utf-8") -> [list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def load_data(data: list[dict[str, any]], model) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: dict[str, list[dict[str]]] = read_json("data.json")

    with create_app(Config).app_context():
        db.drop_all()
        db.create_all()

        load_data(fixtures['genres'], Genre)
        load_data(fixtures['directors'], Director)
        load_data(fixtures['movies'], Movie)

        with suppress(IntegrityError):
            db.session.commit()

