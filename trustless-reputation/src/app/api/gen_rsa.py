from Cryptodome.PublicKey import RSA

def gen_RSA_key_pair(bits=2048, e=65537):
    
    key_pair = RSA.generate(bits, e)
    pubKey = key_pair.publickey().exportKey()
    priKey = key_pair.exportKey()
    
    return pubKey, priKey
