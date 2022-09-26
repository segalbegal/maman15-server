from constants import MSG_CODE_LEN
from utilities.socket_utils import SocketUtils as su
import socket

class ClientHandler:
    def __init__(self, parsers: dict, message_handlers: dict) -> None:
        self.message_parsers: dict = parsers
        self.message_handlers: dict = message_handlers

    def handle_client(self, client_sock: socket.socket) -> None:
        message_code: int = su.read_number_from_socket(client_sock, MSG_CODE_LEN)
        parsed_message: dict = self.message_parsers[message_code].parse_message(client_sock)
        self.message_handlers[message_code].handle_message(parsed_message, client_sock)
