import uuid
from hashlib import sha256

from Cryptodome.PublicKey import RSA
from ecdsa import SigningKey, SECP256k1

from flask_script import Command


from repapp.concept import customer, service_provider

from repapp.customer.models import Customer, CustomerTransaction
from repapp.sprovider.models import SProvider
from repapp.transaction.models import Transaction

from repapp.extensions import sqldb as db


class Demo(Command):

    def run(self):
        print('Here is debug script!!!')

        ecdsa_keypair = SigningKey.generate(curve=SECP256k1, hashfunc=sha256)

        trans = db.session.query(Transaction).filter(Transaction.id == 1).first()
        cus = db.session.query(Customer).filter(Customer.id == 1).first()
        cus_trans = db.session.query(CustomerTransaction).filter(CustomerTransaction.id == 2).first()
        sprovider = db.session.query(SProvider).filter(SProvider.id == 1).first()

        # sprovider.d = sp.d
        # sprovider.e = sp.e
        # sprovider.n = sp.n
        # sprovider.privkey = (sp.privatekey).hex()
        # sprovider.pubkey = (sp.pubkey).hex()


        # import ipdb
        # ipdb.set_trace()

    # def RSA_demo(message, keypair):
        
        # Use 1024 bits as simplest example with e=3
        from Cryptodome.PublicKey import RSA
        
        rsa_keypair = RSA.generate(1024, e=3)
        rsa_pubkey = rsa_keypair.publickey().export_key()


        from base64 import b64decode,b64encode

        key_der = b64decode(rsa_pubkey)

        from repapp.common.utils import get_token

        get_token(cus_trans.pubkey, 'sp1', rsa_pubkey, 'transx')

        import ipdb
        ipdb.set_trace()