from socket import socket
from message_parsers.message_parser import MessageParser
from utilities.socket_utils import SocketUtils as su
from constants import NAME_LEN, PUBLIC_KEY_LEN

class PublicKeyMessageParser(MessageParser):
    def parse_message(self, client_sock: socket) -> dict:
        return {
            'name': su.read_text_from_socket(client_sock, NAME_LEN),
            'public-key': su.read_bytes_from_socket(client_sock, PUBLIC_KEY_LEN),
        }
