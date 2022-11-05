from message_handlers.message_handler import MessageHandler
from data.data_holder import DataHolder
from constants.statuses import REGISTER_SUCC_STATUS, REGISTER_FAIL_STATUS
import uuid

class RegisterMessageHandler(MessageHandler):
    def __init__(self, data: DataHolder):
        self.data: DataHolder = data

    def handle_message(self, message: dict) -> dict:
        if self.data.user_exists(message['name']):
            return {'status': REGISTER_FAIL_STATUS}

        message['id'] = uuid.uuid1().bytes
        self.data.insert_user(message)

        return {'status': REGISTER_SUCC_STATUS, 'id': message['id']}
