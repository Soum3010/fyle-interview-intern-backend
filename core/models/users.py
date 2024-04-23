from core import db
from sqlalchemy import Column,String,Sequence,TIMESTAMP,Integer
from core.libs import helpers


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, db.Sequence('users_id_seq'), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<User %r>' % self.username