from Crypto.Cipher import AES
import hashlib
import random
import os
from base64 import b64encode


def true_random16():
    saltybit = os.urandom(16)
    return saltybit


def true_iv():
    iv = os.urandom(16)
    return iv


def true_fill():
    hashybit = hashlib.sha512(true_random16()).digest()
    return hashybit


def true_encrypt(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    padding = true_fill()
    to_encrypt = bytes(data, 'utf-8')
    fill = b'|' + padding[len(to_encrypt) + 1:]
    to_encrypt = to_encrypt + fill
    print(to_encrypt)
    data_crypt = aes.encrypt(to_encrypt)
    return data_crypt


def true_decrypt(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv, )
    open_secret = aes.decrypt(data)
    open_secret = open_secret.split(b'|')[0]
    return open_secret

