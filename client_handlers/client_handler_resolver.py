import socket
from client_handlers.client_handler import ClientHandler
from message_parsers.message_parser import MessageParser

class ClientHandlerResolver(ClientHandler):
    def __init__(self, parser: MessageParser, handlers: dict, default_handler: ClientHandler):
        self.message_parser: MessageParser = parser
        self.handlers: dict = handlers
        self.default_handler: ClientHandler = default_handler

    def handle_client(self, client_sock: socket.socket, message: dict = None) -> None:
        parsed_message = self.message_parser.parse_message(client_sock)

        if parsed_message['msg-code'] in self.handlers:
            self.handlers[parsed_message['msg-code']].handle_client(client_sock, parsed_message)
        else:
            self.default_handler.handle_client(client_sock, parsed_message)
