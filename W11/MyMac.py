__mydoc__ = """
MyMac.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenge:

C1. Implement gen_key() to generate random 256 bits
C2. Implement get_hmac(key, plaintext_utf8) to message digest hmac
C3. Implement verify_hmac(key, plaintext_utf8, hmacMd) to compare hmacMd with hmac generated using key and plaintext_utf8

"""


from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes


def gen_key():
    # Change C1: Generate random key of 256 bits
    #keyBytes = ...
    #return keyBytes



def get_hmac(key, plaintext_utf8):
    # Change C2: Generate HMAC
    #hmac = ...
    # Change C2: update hmac with plaintext
    #hmac.....
    # Change C2: generate hexidecimal hmac
    #hmacMd = ....
    #return hmacMd


def verify_hmac(key, plaintext_utf8, hmacMd):
    # Change C3: Generate HMAC
    #computed_hmac ....
    # Change C3: update hmac with plaintext
    #computed_hmac....
    # Change C3: generate hexidecimal hmac
    #computed_hmacMd = ....
    # Change C3: Compare hmac with computed hmac
    #if (....):
    #    return "Matched"
    #else:
    #    return "Not Matched"
