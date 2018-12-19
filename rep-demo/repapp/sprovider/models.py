
from sqlalchemy import Column, Integer, String, Text, BigInteger
from sqlalchemy.orm import relationship, backref

from repapp.extensions import sqldb as db

class SProvider(db.Model):
    
    __tablename__ = 'sproviders'

    id = Column(Integer, primary_key=True)
    identifier = Column(String(), nullable=False)

    pubkey = Column(Text, nullable=False)
    privkey = Column(Text, nullable=False)
    # e = Column(String, nullable=False)
    # n = Column(String, nullable=False)
    # d = Column(String, nullable=False)

    transactions = relationship('Transaction', backref="sproviders")

    def __repr__(self):
        return '<SProvider %r | %r>' % (self.id, self.identifier)