from message_handlers.message_handler import MessageHandler
from data.data_holder import DataHolder
from constants.statuses import PUBLIC_KEY_STATUS

import utilities.crypto.aes_public_utils as aes
import utilities.crypto.rsa_public_utils as rsa


class PublicKeyMessageHandler(MessageHandler):
    def __init__(self, data: DataHolder):
        self.data: DataHolder = data

    def handle_message(self, message: dict) -> dict:
        try:
            key = self.data.get_user_aes(message)
            message['aes-key'] = key
        except Exception as e:
            key, encryptor = aes.generate_key()
            message['aes-key'] = key
            self.data.update_user_cred(message)

        encrypted_key = rsa.encrypt_pub_key(key, message['public-key'])
        return {
            'status': PUBLIC_KEY_STATUS,
            'name': message['name'],
            'aes-key': encrypted_key,
            'public-key': message['public-key'],
            'id': message['id'],
        }
