from socket import socket
from constants import NAME_LEN
from utilities.socket_utils import SocketUtils as su

class RegisterMessageParser:
    def parse_message(self, client_sock: socket) -> dict:
        name = su.read_text_from_socket(client_sock, NAME_LEN)
        return {'name': name}