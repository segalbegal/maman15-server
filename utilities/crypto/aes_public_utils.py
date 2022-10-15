from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from constants import AES_KEY_LEN

IV_BLOCK_LEN = 16
IV_BLOCK_VALUE = 0

def generate_key() -> tuple:
    key = get_random_bytes(AES_KEY_LEN)
    return key, AES.new(key, AES.MODE_CBC)

def decrypt(data: bytes, pub_aes_key: bytes) -> bytes:
    iv = [IV_BLOCK_VALUE for _ in range(IV_BLOCK_LEN)]
    cipher = AES.new(pub_aes_key, AES.MODE_CBC, bytes(iv))
    return cipher.decrypt(data)
