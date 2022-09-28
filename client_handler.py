from constants import MSG_CODE_LEN
from utilities.socket_utils import SocketUtils as su
import socket
from message_parsers.message_parser import MessageParser

class ClientHandler:
    def __init__(self, parser: dict, message_handlers: dict) -> None:
        self.message_parser: MessageParser = parser
        self.message_handler:
        self.message_handlers: dict = message_handlers

    def handle_client(self, client_sock: socket.socket) -> None:
        parsed_message: dict = self.message_parser.parse_message(client_sock)
        response: dict = self.message_handlers[message_code].handle_message(parsed_message, client_sock)
