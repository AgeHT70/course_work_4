# from marshmallow import Schema, fields
#
# from setup_db import db
#
#
# class UserMovie(db.Model):
#     __tablename__ = 'user_movie'
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
#     movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)
#
#
# class UserMovieSchema(Schema):
#     user_id = fields.Int()
#     movie_id = fields.Str()
#
