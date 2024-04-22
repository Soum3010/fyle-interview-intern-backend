from core import db
from sqlalchemy import Integer,Column,Sequence,ForeignKey,TIMESTAMP
from core.libs import helpers


class Principal(db.Model):
    __tablename__ = 'principals'
    id = Column(Integer, Sequence('principals_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Principal %r>' % self.id
    
    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()