from flask_login import UserMixin
from create import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class ActiveUsers(UserMixin, db.Model):
    email = db.Column(db.String(100), primary_key=True)
    login_timestamp = db.Column(db.DateTime, default=db.func.now())
