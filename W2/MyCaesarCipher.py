__mydoc__ = """
MyCaesarCipher.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenges:
----------
C1. Implement encrypt() and decrypt() to handle only upper case, 

C2. Enhance encrypt() and decrypt() to handle both upper and lower cases, 

C3. Enhance encrypt() and decrypt() to handle all base64 characters, 

"""

# Change: According to C1, C2, C3
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    


def encrypt(key, plaintext_utf8):
    ciphertext_utf8 = ""

    for character in plaintext_utf8:
        if character in LETTERS:
            # Change: get the character position
            #position = ... # hint: use find()
            #position = position + ...

            # Change: wrap-around if position >= length of LETTERS
            #if position >= len(LETTERS):
                #position = position - ...

            # Change: append encrypted character
            #ciphertext_utf8 = ciphertext_utf8 + ...

        else:
            # Change: append character without encrypting
            #ciphertext_utf8 = ciphertext_utf8 + ...

    return ciphertext_utf8


def decrypt(key, ciphertext_utf8):
    decryptedtext_utf = ""

    for character in ciphertext_utf8:
        if character in LETTERS:
            # Change: get the character position
            #position = ... # hint: use find()
            #position = position - ...

            # Change: wrap-around if position >= length of LETTERS
            #if position < 0:
                #position = position + ...

            # Change: append encrypted character
            #decryptedtext_utf = decryptedtext_utf + ...

        else:
            # Change: append character without encrypting
            #decryptedtext_utf = decryptedtext_utf + ...

    return decryptedtext_utf
