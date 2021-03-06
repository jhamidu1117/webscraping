from Crypto.Cipher import AES
import hashlib
import random
import os
from base64 import b64encode, b64decode

SECRET_KEY = 'chicken_da_corn_say_da_corn_cant_grow_uh_huh'


def __random5():
    """ Generate a random sequence of 5 bytes for use in a SHA512 hash. """
    return bytes(''.join(map(chr, random.sample(range(255), 5))), 'utf-8')


def __fill():
    """ This is used to generate filler data to pad our plain text before encryption. """
    return hashlib.sha512(__random5()).digest()


def __cipher():
    """ A simple constructor we can call from both our encrypt and decrypt functions. """
    key = hashlib.sha256(bytes(SECRET_KEY, 'utf-8')).digest()  # Key is generated by our SECRET_KEY in Django.
    return AES.new(key, mode=2)
    # Here you should perhaps use MODE_CBC, and add an initialization vector for additional security.  ECB is the default, and isn't very secure.


def encrypt(data):
    """ The entrypoint for encrypting our field. """
    FILL = __fill() + __fill() + __fill()  # This is used to generate filler so we can satisfy the block size of AES.  It is best to pad with random data, than to pad with say nulls.
    return __cipher().encrypt(bytes(data, 'utf-8') + b'|' + FILL[len(data) + 1:])


def decrypt(data):
    """ Entrypoint for decryption """

    return __cipher().decrypt(data).split(b'|')[0].decode('utf-8')


def true_random16():
    saltybit = os.urandom(16)
    return saltybit


def true_key(phrase):
    key = hashlib.md5(bytes(phrase, 'utf-8')).digest()
    key = key[:16]
    return key


def true_iv(phrase):
    iv = hashlib.md5(bytes(phrase, 'utf-8')).digest()
    iv = iv[:16]
    return iv


def true_fill():
    hashybit = hashlib.sha512(bytes(SECRET_KEY, 'utf-8')).digest()
    return hashybit


def true_encrypt(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    padding = true_fill()
    to_encrypt = bytes(data, 'utf-8')
    fill = b'|' + padding[len(to_encrypt) + 1:]
    to_encrypt = to_encrypt + fill
    data_crypt = aes.encrypt(to_encrypt)
    data_crypt = b64encode(data_crypt).decode()
    return data_crypt


def true_decrypt(key, iv, data):
    aes = AES.new(key, AES.MODE_CBC, iv)
    data = data.encode('ascii')
    data = b64decode(data)
    open_secret = aes.decrypt(data)
    open_secret = open_secret.split(b'|')[0]
    return open_secret.decode()


if __name__ == '__main__':
    pass_phrase = 'chicken_da_corn'
    key_phrase = 'user_name_hash'
    iv_phrase = 'email_hash'
    my_true_key = true_key(key_phrase)
    my_true_iv = true_iv(iv_phrase)
    secret_pass = true_encrypt(key=my_true_key, iv=my_true_iv, data=pass_phrase)
    secret_open = true_decrypt(key=my_true_key, iv=my_true_iv, data=secret_pass)
    print(secret_open)
