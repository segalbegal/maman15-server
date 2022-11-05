from socket import socket
from message_handlers.message_handler import MessageHandler

class MessageHandlerResolver(MessageHandler):
    def __init__(self, handlers: dict, default_handler: MessageHandler):
        self.handlers: dict = handlers
        self.default_handler: MessageHandler = default_handler

    def handle_message(self, message: dict) -> dict:
        msg_code = message['msg-code']
        return self.handlers[msg_code].handle_message(message) \
            if msg_code in self.handlers \
            else self.default_handler.handle_message(message)
