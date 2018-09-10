# from hashlib import sha256
# from crypt import sha256
import random
from Cryptodome.Hash import SHA256
import crypt 

from Cryptodome.PublicKey import RSA
# PKCS1_OAEP is a replacement from the encrypt method of RSA
from Cryptodome.Cipher import PKCS1_OAEP
def get_token(pubkey, provider_identifier, provider_pubkey, transaction_identifier):
    
    # Same with customer pubkey, try to convert key to bytes and processing all by bytes objects
    provider_pubkey = bytes.fromhex(provider_pubkey)
    sp_pubkey_obj = RSA.importKey(provider_pubkey)

    # Assume that pubkey in hex format, we need convert it to bytes before hashing
    pubkey = bytes.fromhex(pubkey)
    # cipher = PKCS1_OAEP.new(sp_pubkey_obj)

    m1 = SHA256.new(pubkey).digest()
    # print('<<m1><<hex>> ', (m1).hex())
    m1 = int.from_bytes(m1, byteorder='big')

    r = random.randrange(0, sp_pubkey_obj.n)
    m1 = m1 * r ** sp_pubkey_obj.e % sp_pubkey_obj.n
    print('<<m1>> ', m1)
    print('<<r>> ', r)

    # send((m1, transaction_identifier), provider_identifier)
    return m1, r
    


def issue_token(customer_identifier, encrypted_msg, provider_prikey, transaction_identifier):

    provider_prikey = bytes.fromhex(provider_prikey)
    sp_key_obj = RSA.import_key(provider_prikey)

    blind_token = encrypted_msg ** sp_key_obj.d % sp_key_obj.n
    print('<<blind_token>>', blind_token)

    # send(blind_token, customer_identifier)
    return blind_token


def unblind_token(blind_token, provider_pubkey, r):
    provider_pubkey = bytes.fromhex(provider_pubkey)
    sp_key_obj = RSA.import_key(provider_pubkey)

    # Token exactly the sign from Provider
    token = blind_token * r ** -1 % sp_key_obj.n
    print('<<token>>', token)
    
    return token

def verify_blind_token(blind_token, provider_pubkey, message):
    provider_pubkey = bytes.fromhex(provider_pubkey)
    sp_key_obj = RSA.import_key(provider_pubkey)

    message_hash = SHA256.new(message).digest()
    message_hash_int = int.from_bytes(message_hash, byteorder='big')

    original_msg = blind_token ** sp_key_obj.e % sp_key_obj.n

    print('\n message_hash_int>> ', message_hash_int)
    print(' original_msg>> ', original_msg)

    return original_msg == message_hash_int

def verify_blind_token_signner(blind_token, provider_prikey, message):
    
    provider_prikey = bytes.fromhex(provider_prikey)
    sp_key_obj = RSA.import_key(provider_prikey)

    message_hash = SHA256.new(message).digest()
    message_hash_int = int.from_bytes(message_hash, byteorder='big')

    signned_msg = message_hash ** sp_key_obj.d % sp_key_obj.n

    print('\n message_hash_int>> ', message_hash_int)
    print(' signned_msg>> ', original_msg)

    return signned_msg == message_hash_int


