from socket import socket

from message_parsers.message_parser import MessageParser
from message_parsers.headers_message_parser import HeaderMessageParser

class MessageParserResolver(MessageParser):
    def __init__(self, headers_parser: HeaderMessageParser, inner_parsers: dict):
        self.headers_parser = headers_parser
        self.inner_parsers = inner_parsers

    def parse_message(self, client_sock: socket) -> dict:
        headers = self.headers_parser.parse_message(client_sock)
        parsed_message: dict = self.inner_parsers[headers['msg-code']].parse_message(client_sock)

        return headers | parsed_message
