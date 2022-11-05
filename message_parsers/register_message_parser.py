from message_parsers.message_parser import MessageParser
from utilities.bytes_utils import BytesUtils as bu
from constants import sizes

class RegisterMessageParser(MessageParser):
    def parse_message(self, data: bytes) -> dict:
        return {'name': bu.extract_text_from_buffer(data, sizes.NAME_LEN, offset=sizes.HEADERS_LEN)}
