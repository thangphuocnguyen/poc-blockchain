from hashlib import sha256

from Cryptodome.PublicKey import RSA
# PKCS1_OAEP is a replacement from the encrypt method of RSA
from Cryptodome.Cipher import PKCS1_OAEP

def get_token(pubkey, provider_identifier, provider_pubkey, transaction_identifier):
    
    pubkey = pubkey.encode('utf8')
    m1 = sha256(pubkey).hexdigest()




    sp_pubkey_obj = RSA.importKey(provider_pubkey)
    cipher = PKCS1_OAEP.new(sp_pubkey_obj)
    # Encrypt the message base on service provider PubKey
    encrypted_message = cipher.encrypt(m1)
