from message_parsers.message_parser import MessageParser
from message_parsers.headers_message_parser import HeaderMessageParser

class MessageParserResolver(MessageParser):
    def __init__(self, headers_parser: HeaderMessageParser, inner_parsers: dict):
        self.headers_parser: HeaderMessageParser = headers_parser
        self.inner_parsers: dict = inner_parsers

    def parse_message(self, data: bytes) -> dict:
        headers = self.headers_parser.parse_message(data)
        msg_code = headers['msg-code']
        payload = self.inner_parsers[msg_code].parse_message(data) if msg_code in self.inner_parsers else {}
        return headers | payload
