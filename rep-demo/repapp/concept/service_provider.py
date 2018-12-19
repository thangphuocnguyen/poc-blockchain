from repapp.common import crypto
from Cryptodome.PublicKey import RSA

class ServiceProvider(object):

    def __init__(self, identifier: str, bits:int=2048, exponent:int=65537):
        self.identifier = identifier
        key_pair = RSA.generate(bits, e=exponent)
        self.pubkey = key_pair.publickey().exportKey()
        self.privatekey = key_pair.exportKey()
        self.e = key_pair.e
        self.n = key_pair.n
        self.d = key_pair.d
        self.key_pair = key_pair
        # import ipdb
        # ipdb.set_trace()

    
    # # def verify(self, message):
    # #     self.key_pair.verify()

    # def issue_token(self, customer_identifier, m1, x):
    #     # TODO: verify transaction identifier first

    #     token = m1 ** self.d % self.n

    #     import ipdb
    #     ipdb.set_trace()

