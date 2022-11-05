from message_handlers.message_handler import MessageHandler
from constants.system_constants import VERSION
from constants.statuses import MESSAGE_APPROVED_STATUS

class DummyMessageHandler(MessageHandler):
    def handle_message(self, message: dict) -> dict:
        return {
            'status': MESSAGE_APPROVED_STATUS,
            'version': VERSION,
        }