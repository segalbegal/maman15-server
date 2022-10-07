from message_handlers.message_handler import MessageHandler
from data.data_holder import DataHolder
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from constants import PUBLIC_KEY_STATUS

AES_KEY_LEN = 32

def generate_aes_key():
    key = get_random_bytes(AES_KEY_LEN)
    return key, AES.new(key, AES.MODE_EAX)

class PublicKeyMessageHandler(MessageHandler):
    def __init__(self, data: DataHolder):
        self.data: DataHolder = data

    def handle_message(self, message: dict) -> dict:
        key, encryptor = generate_aes_key()
        message['aes-key'] = key
        self.data.update_user_cred(message)

        pub_key = RSA.importKey(message['public-key'])
        cipher = PKCS1_OAEP.new(pub_key)
        encrypted_key = cipher.encrypt(key)

        return {
            'status': PUBLIC_KEY_STATUS,
            'name': message['name'],
            'aes-key': encrypted_key,
            'public-key': message['public-key'],
            'id': message['id'],
        }
