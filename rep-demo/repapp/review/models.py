from repapp.extensions import sqldb as db
from sqlalchemy import Column, Integer, String, Text, BigInteger


class Review(db.Model):
    
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)

    addr = Column(String, nullable=False)
    pubkey = Column(String, nullable=False)
    token = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    review = Column(Text, nullable=False)
    sig = Column(String, nullable=False)
    pointer = Column(String, nullable=False)

    def __repr__(self):
        return '<Review %r' % (self.id)