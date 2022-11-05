from message_parsers.message_parser import MessageParser
from constants.sizes import HEADERS_LEN, NAME_LEN, PUBLIC_KEY_LEN
from utilities.bytes_utils import BytesUtils as bu

class PublicKeyMessageParser(MessageParser):
    def parse_message(self, data: bytes) -> dict:
        return {
            'name': bu.extract_text_from_buffer(data, HEADERS_LEN, NAME_LEN),
            'public-key': bu.subbuf(data, HEADERS_LEN + NAME_LEN, PUBLIC_KEY_LEN),
        }
