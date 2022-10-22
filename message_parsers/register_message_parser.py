from socket import socket
from constants.sizes import NAME_LEN
from utilities.socket_utils import SocketUtils as su
from message_parsers.message_parser import MessageParser

class RegisterMessageParser(MessageParser):
    def parse_message(self, client_sock: socket) -> dict:
        return {'name': su.read_text_from_socket(client_sock, NAME_LEN)}
