import base64
import io
import os
import zlib
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA


class Crypto:

    def __init__(self, file_path):
        with open(file_path, 'rb') as f:
            self.key = RSA.import_key(f.read())

    def decrypt(self, data):
        byte_stream = io.BytesIO(base64.b64decode(data))

        encryptedSessionKey = byte_stream.read(self.key.size_in_bytes())
        nonce = byte_stream.read(16)
        tag = byte_stream.read(16)
        ciphertext = byte_stream.read()

        # decrypt the session key
        cipher = PKCS1_OAEP.new(self.key)
        sessionKey = cipher.decrypt(encryptedSessionKey)

        # decrypt the data with the session key
        cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()
