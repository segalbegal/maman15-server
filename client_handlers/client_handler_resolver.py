import socket
from client_handlers.client_handler import ClientHandler
from message_parsers.message_parser import MessageParser
from socket_readers.socket_reader import SocketReader

class ClientHandlerResolver(ClientHandler):
    def __init__(self, socket_reader: SocketReader, message_parser: MessageParser, handlers: dict, default_handler: ClientHandler):
        self.socket_reader: SocketReader = socket_reader
        self.message_parser: MessageParser = message_parser
        self.handlers: dict = handlers
        self.default_handler: ClientHandler = default_handler

    def handle_client(self, client_sock: socket.socket, message: dict = None) -> None:
        serialized_message = self.socket_reader.read_bytes_from_socket(client_sock)
        parsed_message = self.message_parser.parse_message(serialized_message)

        if parsed_message['msg-code'] in self.handlers:
            self.handlers[parsed_message['msg-code']].handle_client(client_sock, parsed_message)
        else:
            self.default_handler.handle_client(client_sock, parsed_message)
