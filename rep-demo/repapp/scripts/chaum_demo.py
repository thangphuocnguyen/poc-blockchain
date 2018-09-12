import uuid
# from hashlib import sha256

from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from ecdsa import SigningKey, SECP256k1

from flask_script import Command


from repapp.concept import customer, service_provider

from repapp.customer.models import Customer, CustomerTransaction
from repapp.sprovider.models import SProvider
from repapp.transaction.models import Transaction

from repapp.extensions import sqldb as db
from repapp.common.chaum_utils import get_token, issue_token, unblind_token, verify_blind_token, verify_blind_token_signner


class Demo(Command):

    def run(self):
        print('Here is Chaum Blind Token demo!!!')
        
        # Please specs the demo_data id that you got from `gendb`
        data_id = 5

        trans = db.session.query(Transaction).filter(Transaction.id == data_id).first()
        cus = db.session.query(Customer).filter(Customer.id == data_id).first()
        cus_trans = db.session.query(CustomerTransaction).filter(CustomerTransaction.id == data_id).first()
        sprovider = db.session.query(SProvider).filter(SProvider.id == data_id).first()

        trans_id = trans.identifier
        sp_id = sprovider.identifier

        # S1: Customer side
        # ----------------------------------------------------------------------
        encrypted_msg, r = get_token(cus_trans.pubkey, sp_id, sprovider.pubkey, trans_id)

        # Customer sent blinded_msg to Provider
        cus_blinded_msg = encrypted_msg
        # S2: Sprovider side
        # ----------------------------------------------------------------------
        # Provider sign to the blinded message that Customer sent (make blind token)
        blind_token = issue_token(cus.identifier, cus_blinded_msg, sprovider.privkey, trans_id)

        # Provider sent blink_token to Customer
        sp_blind_token = blind_token


        
        # S3: Customer side
        # ----------------------------------------------------------------------
        token = unblind_token(sp_blind_token, sprovider.pubkey, r)
        # Customer verifying the token
        cus_ver_result = verify_blind_token(token, sprovider.pubkey, cus_trans.pubkey)
        print('\n!!!Customer side verifying token successed: ', cus_ver_result)

        
        # Provider verifying token
        pro_ver_result = verify_blind_token_signner(token, sprovider.privkey, cus_trans.pubkey)
        print('\n!!!Provider side verifying token successed: ', pro_ver_result)
        
        # import ipdb
        # ipdb.set_trace()
