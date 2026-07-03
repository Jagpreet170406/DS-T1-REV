__mydoc__ = """
MyRsa.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenges:

C1. Implement generate_keypair(keySize) to return keyPair of keySize bits

C2. Implement get_private_key(keypair) to extract private key from keyPair

C3. Implement get_public_key(keypair) to extract public key from keyPair

C4. Implement write_private_key(keypair, private_keyfile) 

C5. Implement write_public_key(keypair, public_keyfile)

C6. Implement read_private_key(private_keyfile)

C7. Implement read_public_key(public_keyfile)

C8. Implement encrypt(public_key, plaintext_utf8)

C9. Implement decrypt(private_key, ciphertext_utf8)

----------
"""


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keypair(keySize):
    # Change C1: Generate keypair
    #keyPair = 
    #return keyPair


def get_private_key(keypair):
    # Change C2: Get Private Key from kepair
    #privatekey =
    #privatekeyObj =
    #return privatekeyObj


def get_public_key(keypair):
    # Change C3: Get Public Key from kepair
    #publickey =
    #publickeyObj =
    #return publickeyObj


def write_private_key(keypair, privatekeyFile):
    # Change C4: extract private key
    #privatekey = ...
    # Change : write private key to file
    #privateFile = ...
    #...
    #return


def write_public_key(keypair, publickeyFile):
    # Change C5: extract public key
    #publickey = ...
    # Change : write public key to file
    #publicFile = ...
    #...
    #return


def read_private_key(privatekeyFile):
    # Change C6: extract private key from File
    #privatekeyObj = ...
    #return privatekeyObj


def read_public_key(publickeyFile):
    # Change C7: extract public key from File
    #publickeyObj = ...
    #return publickeyObj


def encrypt(publickey, plaintext):
    # Change C8: create RSA with public key
    #rsa = ...
    # Change : encrypt plaintext
    #ciphertextBytes = ...
    # Change : encode ciphertext to base64
    #ciphertextBase64 = ...
    #return ciphertextBase64


def decrypt(privatekey, ciphertextBase64):
    # Change C9: create RSA with private key
    #rsa = ...
    # Change : Change ciphertext from base64 to bytes
    #ciphertextBytes = ...
    # Change : Decrypt ciphertext bytes to decrypted text
    #decryptedtext = ...
    #return decryptedtext
