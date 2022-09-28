from message_parser import MessageParser
from utilities.socket_utils import SocketUtils as su
import constants

class HeaderMessageParser(MessageParser):
    def parse_message(self, client_sock: socket) -> dict:
        details = {}
        details['id'] = su.read_bytes_from_socket(client_sock, constants.ID_LEN)
        details['version'] = su.read_number_from_socket(client_sock, constants.VERSION_LEN)
        details['message-code'] = su.read_number_from_socket(client_sock, constants.MSG_CODE_LEN)
        payload_len = su.read_number_from_socket(client_sock, constants.PAYLOAD_SIZE_LEN) # don't actually needs this

        return details