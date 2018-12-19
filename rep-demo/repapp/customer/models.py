
from Cryptodome.PublicKey import RSA
from ecdsa import SigningKey, SECP256k1
from hashlib import sha256

from repapp.extensions import sqldb as db
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

from repapp.transaction.models import Transaction


class Customer(db.Model):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    identifier = Column(String, nullable=False)

    transactions = relationship('CustomerTransaction', backref="customers")

    # def get_token(self, transaction_identifier, sp_e, sp_n, sp_identifier)
    def __repr__(self):
        return '<Customer %r | %r>' % (self.id, self.identifier)


class CustomerTransaction(db.Model):

    __tablename__ = 'customer_transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)

    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    # customer = relationship("Customer")

    trans_identifier = Column(String, nullable=False, server_default=None)

    pubkey = Column(Text, nullable=False, server_default=None)
    privkey = Column(Text, nullable=False, server_default=None)

    # bidirectional attribute/collection of "customer"/"customer_transactions"
    # customer = relationship(Customer, backref=backref(
    #     "customer_transactions", cascade="all, delete-orphan"))

    # reference to the "Transaction" object
    # transaction = relationship("Transaction")
    def __repr__(self):
        return '<CustomerTransaction %r | %r>' % (self.id, self.identifier)