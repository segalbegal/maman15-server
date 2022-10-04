from socket import socket

class MessageHandler:
    def handle_message(self, message: dict, client_sock: socket) -> dict:
        raise NotImplementedError()