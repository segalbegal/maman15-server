from socket import socket

class MessageParser:
    def parse_message(self, client_sock: socket) -> dict:
        raise NotImplementedError()
