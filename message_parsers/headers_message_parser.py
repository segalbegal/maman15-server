from message_parsers.message_parser import MessageParser
from utilities.bytes_utils import BytesUtils as bu
from constants import sizes

class HeaderMessageParser(MessageParser):
    def parse_message(self, data: bytes) -> dict:
        details = {
            'id': data[:sizes.ID_LEN],
            'version': bu.extract_num_from_buffer(data, sizes.VERSION_LEN, sizes.ID_LEN),
            'msg-code': bu.extract_num_from_buffer(data, sizes.MSG_CODE_LEN, sizes.VERSION_LEN + sizes.ID_LEN)
        }

        return details
