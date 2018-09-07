from repapp.common import crypto
from Cryptodome.PublicKey import RSA
from ecdsa import SigningKey, SECP256k1
from hashlib import sha256
import random
import sys

class Customer(object):

    # RSA keygen
    # def __init__(self, name: str, bits:int=2048, exponent:int=65537):
    #     self.name = name
    #     key_pair = RSA.generate(bits, e=exponent)
    #     self.pubkey = key_pair.publickey().exportKey()
    #     self.privatekey = key_pair.exportKey()
    #     self.e = key_pair.e
    #     self.n = key_pair.n

    # ECDSA keygen (SECP256k1)
    def __init__(self, name: str):

        sk = SigningKey.generate(curve=SECP256k1, hashfunc=sha256)

        self.privkey = sk
        self.pubkey = sk.get_verifying_key().to_string()

    
    def get_token(self, transaction_identifier, sp_e, sp_n, sp_identifier, send_func):
        m1 = self.pubkey

        _random = random.randrange(0, sp_n)
        m1 = int.from_bytes(m1, byteorder=sys.byteorder)
        m1 = m1 * _random ** sp_e % sp_n

        # import ipdb
        # ipdb.set_trace()

        send_func((m1, transaction_identifier), sp_identifier)

        return (m1, _random)
    
    def get_reputation(self, sp_identifier):
        return 20
    
    



