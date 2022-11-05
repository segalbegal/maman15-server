from message_parsers.message_parser import MessageParser
from utilities.bytes_utils import BytesUtils as bu
from constants.sizes import ID_LEN, FILE_NAME_LEN, HEADERS_LEN

class CRCMessageParser(MessageParser):
    def parse_message(self, data: bytes) -> dict:
        return {
            'id': bu.subbuf(data, HEADERS_LEN, ID_LEN),
            'file-name': bu.extract_text_from_buffer(data, FILE_NAME_LEN, HEADERS_LEN + ID_LEN),
        }
