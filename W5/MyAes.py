__mydoc__ = """
MyAes.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenges:
----------
C1. Implement genKey(keySize) to return Base64 of random size = keySize x 8 bits.

C2. Implement AES encrypt(keyBase64, plaintext) where:
- keyBase64: AES key in Base64 format
- plaintext_utf8: plaintext in UTF8 format
- assumption: use CBC mode, IV and default padding (PKCS7)
- return: iv and cipherText in Base64 format

C3. Implement AES decrypt(ivBase64, keyBase64, ciphertextBase64) where:
- ivBase64: iv in Base64 format
- keyBase64: AES key in Base64 format
- ciphertextBase64: ciphertext in Base64 format
- assumption: use CBC mode and default padding (PKCS7)
- return: decryptedtext

C4. Implement AES encryptToFile(keyBase64, plaintext, filename) where:
- keyBase64: AES key in Base64 format
- plaintext_utf8: plaintext in UTF8 format
- create filename
- assumption: use CBC mode, IV and default padding (PKCS7)
- return: nil

C5. Implement AES decryptFromFile(keyBase64, filename) where:
- keyBase64: AES key in Base64 format
- filename is name of file with iv and ciphertext
- assumption: use CBC mode, IV and default padding (PKCS7)
- return: decryptedtext

Check that the ciphertext file (ciphertext.bin) is also created.

Optional:
---------
Modify to support CFB and OFB modes.

"""


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


def genKey(keySize):
    # Change C1: Generate random key of size keySize
    #keyBytes = ....
    # Change C1: Convert key from bytes to base64
    #keyBase64 = ....
    #return keyBase64

# AES encrypt using CBC and IV, with default padding (PKCS7)

def encrypt(keyBase64, plaintext):
    # convert key and plaintext to bytes
    #keyBytes = ...
    #plaintextBytes = ...
    # Change C2: create cypher with key and CBC mode
    #cipher = ...
    # Change C2: create cyphertext in Bytes
    #ciphertextBytes = ...
    # Change C2: capture iv in Bytes
    #ivBytes = ...
    # Change C2: Convert ciphertext and iv from bytes to base64
    #ciphertextBase64 = ...
    #ivBase64 = ...

    #return ivBase64, ciphertextBase64

def decrypt(ciphertextBase64, keyBase64, ivBase64):
    # Change C3: convert key, iv, ciphertext to bytes
    #keyBytes = ...
    #ivBytes = ...
    #ciphertextBytes = ...
    # Change C3: create cypher with key, iv and specify mode
    #cipher = ...
    # Change C3: decrypt ciphertext in decryptedtextBytes
    #decryptedtextBytes = ...
    # Change C3: convert decryptedtext from bytes to ASCII characters
    #decryptedtext = ...
    #return decryptedtext


def encryptToFile(keyBase64, plaintext, fileName):
    # Change C4: convert key and plaintext to bytes
    #keyBytes = ...
    #plaintextBytes = ...
    # Change C4: create cypher with key and specify mode
    #cipher = ...
    # Change C4: create cyphertext and capture IV in bytes
    #ciphertextBytes = ...
    #ivBytes = ...
    # Change C4: write iv and ciphertext bytes to file
    #file_out = ...
    #...
    return


# AES decrypt using CBC and IV, with default unpadding (PKCS7)
def decryptFromFile(keyBase64, fileName):
    # Change C5: convert key and plaintext to bytes
    #keyBytes = ...
    # Change C5: read iv and ciphertext bytes from file
    #fileIn = ...
    #...
    # Change C5: create cypher with key, iv and specify mode
    #cipher = ...
    #decryptedtextBytes = ...
    #decryptedtext = ...
    #return decryptedtext
