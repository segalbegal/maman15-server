from socket import socket
from constants import NAME_LEN
from utilities.socket_utils import SocketUtils as su
from headers_message_parser import HeaderMessageParser

class RegisterMessageParser(HeaderMessageParser):
    def parse_message(self, client_sock: socket) -> dict:
        headers = super().parse_message(client_sock)
        headers['name'] = su.read_text_from_socket(client_sock, NAME_LEN)

        return headers