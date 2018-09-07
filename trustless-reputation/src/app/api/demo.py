""" POC Demo.

"""
from ..core import logger
from ..common import crypto

from Cryptodome.Hash import SHA256
from Cryptodome.Random import random

from app.concept.customer import Customer
from app.concept.service_provider import ServiceProvider
from app.concept.transaction import Transaction
from app.concept.send_fake import fake_send as send


def main():
    """ Execute the command.
    
    """
    print('hello')

    customer = Customer('cus_01')
    service_provider = ServiceProvider('sp_01')
    transaction = Transaction('trs_01')

    # Just demo get sp reputation
    current_sp_reputation = customer.get_reputation('sp_01')
    
    # Asume that service_provider n,e,pubkey is public
    sp_e = service_provider.e
    sp_n = service_provider.n
    sp_identifier = service_provider.identifier
    
    blind_token = customer.get_token(
        transaction.identifier,
        sp_e,
        sp_n,
        sp_identifier,
        send
    )

    import ipdb
    ipdb.set_trace()

    return
