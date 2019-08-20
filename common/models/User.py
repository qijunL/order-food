# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from application import login_manager
from application import db


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.BigInteger, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    mobile = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue())
    email = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue())
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    avatar = db.Column(db.String(64), nullable=False, server_default=db.FetchedValue())
    login_name = db.Column(db.String(20), nullable=False, unique=True, server_default=db.FetchedValue())
    _login_pwd = db.Column('login_pwd', db.String(32), nullable=False, server_default=db.FetchedValue())
    login_salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

    @property
    def id(self):
        return self.uid

    @property
    def login_pwd(self):
        return self._login_pwd

    @login_pwd.setter
    def login_pwd(self, raw):
        self._login_pwd = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._login_pwd, raw)


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
