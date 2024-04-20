
from django.conf import settings
from rest_framework import exceptions

import json 
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class Crypt:
    def __init__(self):
        salt = settings.SALT
        self.salt = salt.encode()
        self.enc_dec_method = 'utf-8'
        self.token_key = settings.TOKEN_KEY

    def encrypt(self, str_to_enc):
        aes_obj = AES.new(self.token_key.encode(), AES.MODE_CFB, self.salt)
        hx_enc = aes_obj.encrypt(str_to_enc.encode())
        mret = b64encode(hx_enc).decode(self.enc_dec_method)
        return mret

    def decrypt(self, enc_str):
        try:
            aes_obj = AES.new(self.token_key.encode(), AES.MODE_CFB, self.salt)
            str_tmp = b64decode(enc_str.encode(self.enc_dec_method))
            str_dec = aes_obj.decrypt(str_tmp)
            mret = str_dec.decode(self.enc_dec_method)
        except:
            msg = 'Invalid token Please relogin.'
            raise exceptions.AuthenticationFailed(msg)
        return mret
    