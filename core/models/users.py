from core import db
from sqlalchemy import Column,String,Sequence,TIMESTAMP,Integer
from core.libs import helpers


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session().query(cls)
        return db_query.filter(*criterion)

    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.filter(cls.email == email).first()
