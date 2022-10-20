from message_handlers.message_handler import MessageHandler
import utilities.crypto.aes_public_utils as aes
from data.data_holder import DataHolder
from utilities.cksum_utils import calculate_crc32
from constants import SEND_FILE_STATUS, VERSION

FILE_PATH = '/files/'

def remove_decryption_postfix(decrypted: bytes):
    tail_len = decrypted[len(decrypted) - 1]
    return decrypted[:-tail_len]

class SendFileMessageHandler(MessageHandler):
    def __init__(self, data_holder: DataHolder):
        self.data_holder: DataHolder = data_holder

    def handle_message(self, message: dict) -> dict:
        client_aes_key = self.data_holder.get_user_aes(message)
        decrypted_file = aes.decrypt(message['content'], client_aes_key)
        decrypted_file = remove_decryption_postfix(decrypted_file)
        file_len = len(decrypted_file)
        crc = calculate_crc32(decrypted_file)

        user_name = self.data_holder.get_user_name(message)
        message['file-path'] = FILE_PATH + user_name
        message['verified'] = False
        self.data_holder.insert_file(message)

        return {
            'status': SEND_FILE_STATUS,
            'version': VERSION,
            'content-size': file_len,
            'file-name': message['file-name'],
            'cksum': crc,
            'id': message['id'],
        }
