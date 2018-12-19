""" Implement the cmd command.

"""
from ..core import logger
from ..common import crypto


def main():
    """ Execute the command.
    
    """
    # Just sample with RSA generation
    print('pubKey: %s \n\npriKey: %s' % crypto.gen_RSA_key_pair())
    return
