from socket import socket
from message_handlers.message_handler import MessageHandler

class MessageHandlerResolver(MessageHandler):
    def __init__(self, handlers: dict):
        self.handlers: dict = handlers

    def handle_message(self, message: dict) -> dict:
        return self.handlers[message['msg-code']].handle_message(message)
