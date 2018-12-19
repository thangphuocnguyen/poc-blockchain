# from hashlib import sha256
# from crypt import sha256

from Cryptodome.Hash import SHA256
import crypt 

from Cryptodome.PublicKey import RSA
# PKCS1_OAEP is a replacement from the encrypt method of RSA
from Cryptodome.Cipher import PKCS1_OAEP
def get_token(pubkey, provider_identifier, provider_pubkey, transaction_identifier):
    
    # Assume that pubkey in hex format, we need convert it to bytes before hashing
    pubkey = bytes.fromhex(pubkey)
    # m1 = sha256(pubkey).digest()
    m1 = SHA256.new(pubkey).digest()

    # import ipdb
    # ipdb.set_trace()

    # Same with customer pubkey, try to convert key to bytes and processing all by bytes objects
    provider_pubkey = bytes.fromhex(provider_pubkey)
    sp_pubkey_obj = RSA.importKey(provider_pubkey)

    cipher = PKCS1_OAEP.new(sp_pubkey_obj)

    # cipher.encrypt()

    # Encrypt the message base on service provider PubKey
    print('<<m1>>', m1)
    encrypted_msg = cipher.encrypt(m1)


    # send(m1, transaction_identifier, provider_identifier)
    
    return encrypted_msg

def issue_token(customer_identifier, encrypted_msg, provider_prikey, transaction_identifier):

    provider_prikey = bytes.fromhex(provider_prikey)
    sp_key_obj = RSA.import_key(provider_prikey)

    from Cryptodome.Signature import pkcs1_15
    from Cryptodome.Hash import SHA256

    hashitem = SHA256.new(encrypted_msg)
    signature = pkcs1_15.new(sp_key_obj).sign(hashitem)

    return signature

def unblind_token(signature_msg, provider_pubkey):
    provider_pubkey = bytes.fromhex(provider_pubkey)
    sp_key_obj = RSA.import_key(provider_pubkey)

    from Cryptodome.Signature import pkcs1_15

    si = pkcs1_15.new(sp_key_obj)

    import ipdb
    ipdb.set_trace()





