from message_parsers.message_parser import MessageParser
from utilities.bytes_utils import BytesUtils as bu
from constants import sizes

class SendFileMessageParser(MessageParser):
    def parse_message(self, data: bytes) -> dict:
        content_size = bu.extract_num_from_buffer(data, sizes.FILE_SIZE_LEN, sizes.HEADERS_LEN + sizes.ID_LEN)
        return {
            'id': bu.subbuf(data, sizes.HEADERS_LEN, sizes.ID_LEN),
            'file-name': bu.extract_text_from_buffer(
                data,
                sizes.FILE_NAME_LEN,
                sizes.HEADERS_LEN + sizes.ID_LEN + sizes.FILE_SIZE_LEN),
            'content': bu.subbuf(
                data,
                sizes.HEADERS_LEN + sizes.ID_LEN + sizes.FILE_SIZE_LEN + sizes.FILE_NAME_LEN,
                content_size),
        }
