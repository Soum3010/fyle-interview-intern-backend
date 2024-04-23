from core import db
from sqlalchemy import Integer,Sequence,ForeignKey,Column,TIMESTAMP
from core.libs import helpers


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Teacher %r>' % self.id
    
    @classmethod
    def get_teachers(cls, principal_id):
        return cls.query.filter_by(user_id=principal_id).all()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()