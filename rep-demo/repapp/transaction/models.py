from sqlalchemy import Column, Integer, String, Text, ForeignKey

from repapp.extensions import sqldb as db

class Transaction(db.Model):
    
    __tablename__ = 'transactions'

    id = db.Column(Integer, primary_key=True)

    identifier = Column(String, nullable=False)
    desc = db.Column(Text, nullable=False)

    sprovider_id = Column(Integer, ForeignKey('sproviders.id'))

    def __repr__(self):
        return '<Transaction %r | %r>' % (self.desc, self.identifier)