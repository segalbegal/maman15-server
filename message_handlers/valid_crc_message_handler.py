from data.data_holder import DataHolder
from message_handlers.message_handler import MessageHandler
from constants.statuses import MESSAGE_APPROVED_STATUS
from constants.system_constants import VERSION

class ValidCrcMessageHandler(MessageHandler):
    def __init__(self, data_holder: DataHolder):
        self.data_holder: DataHolder = data_holder

    def handle_message(self, message: dict) -> dict:
        self.data_holder.update_file_verification(message)
        return {
            'status': MESSAGE_APPROVED_STATUS,
            'version': VERSION,
        }
