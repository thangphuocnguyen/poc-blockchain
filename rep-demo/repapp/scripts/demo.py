import uuid

from flask_script import Command


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
        sprovider = SProvider(
            identifier=str(uuid.uuid4()),
            pubkey='pub',
            privkey='pri',
            e=0,
            n=0,
            d=0
        )
        db.session.add(sprovider)
        db.session.commit()

        # Generate service provider keypair
        sp = service_provider.ServiceProvider(
            'sp01'
        )
        
        # Generate new Transaction in db
        # ----------------------------------------------------------------------
        
        trans = Transaction(
            identifier=str(uuid.uuid4()),
            desc='Transaction'
        )
        sprovider.transactions.append(trans)
        # db.session.add(trans)
        db.session.commit()

        # Generate new Customer
        # ----------------------------------------------------------------------
        cus = Customer(identifier=str(uuid.uuid4()))
        db.session.add(cus)
        db.session.commit()
        
        cus_keypair = customer.Customer(
            cus.identifier
        )

        cus_trans = CustomerTransaction(
                trans_identifier=trans.identifier,
                pubkey=(cus_keypair.pubkey).hex(),
                privkey=(cus_keypair.privkey.to_string()).hex()
            )
        cus.transactions.append(cus_trans)
        db.session.commit()

        

        import ipdb
        ipdb.set_trace()
