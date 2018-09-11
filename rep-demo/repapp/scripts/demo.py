import uuid

from flask_script import Command

from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from ecdsa import SigningKey, SECP256k1

from repapp.concept import customer, service_provider

from repapp.customer.models import Customer, CustomerTransaction
from repapp.sprovider.models import SProvider
from repapp.transaction.models import Transaction

from repapp.extensions import sqldb as db


class Demo(Command):

    def run(self):
        print('Hello')

        # Generate Service Provider
        # ----------------------------------------------------------------------
        # import ipdb
        # ipdb.set_trace()
        # bits = 1024 for normally RSA, e=3 for more ez on sample
        provider_key_pair = RSA.generate(1024, e=3)

        sprovider = SProvider(
            identifier=str(uuid.uuid4()),
            pubkey=(provider_key_pair.publickey().exportKey()).hex(),
            privkey=(provider_key_pair.exportKey()).hex()
        )
        db.session.add(sprovider)
        db.session.commit()
        
        # Generate new Transaction in db
        # ----------------------------------------------------------------------
        
        trans = Transaction(
            identifier=str(uuid.uuid4()),
            desc='Transaction {}'.format(sprovider.identifier)
        )
        sprovider.transactions.append(trans)
        db.session.commit()

        # Generate new Customer
        # ----------------------------------------------------------------------
        cus = Customer(identifier=str(uuid.uuid4()))
        db.session.add(cus)
        # db.session.commit()
        
        # cus_keypair = SigningKey.generate(curve=SECP256k1, hashfunc=SHA256)
        # cus_trans = CustomerTransaction(
        #         trans_identifier=trans.identifier,
        #         pubkey=(cus_keypair.to_string()).hex(),
        #         privkey=(cus_keypair.get_verifying_key().to_string()).hex()
        #     )
        
        # Use RSA keypair for quickly demo
        cus_keypair = RSA.generate(1024, e=3)
        cus_trans = CustomerTransaction(
                trans_identifier=trans.identifier,
                pubkey=(provider_key_pair.publickey().exportKey()).hex(),
                privkey=(provider_key_pair.exportKey()).hex()
            )

        cus.transactions.append(cus_trans)
        db.session.commit()

        print('Customer id {} >> identifier {}'.format(cus.id, cus.identifier))
        print('Customer_Transaction id {} >> identifier {}'.format(cus_trans.id, cus_trans.trans_identifier))
        print('Provider id {} >> identifier {}'.format(sprovider.id, sprovider.identifier))
        print('Transaction id {} >> identifier {}'.format(trans.id, trans.identifier))

