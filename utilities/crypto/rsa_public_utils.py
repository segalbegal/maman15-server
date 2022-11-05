from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_pub_key(key: bytes, data: bytes):
    pub_key = RSA.importKey(data)
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(key)
