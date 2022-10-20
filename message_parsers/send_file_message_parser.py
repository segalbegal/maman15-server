from socket import socket
from message_parsers.message_parser import MessageParser
from utilities.socket_utils import SocketUtils as su
import constants

class SendFileMessageParser(MessageParser):
    def parse_message(self, client_sock: socket) -> dict:
        res = {
            'id': su.read_bytes_from_socket(client_sock, constants.ID_LEN),
        }
        content_size = su.read_number_from_socket(client_sock, constants.FILE_SIZE_LEN)
        res['file-name'] = su.read_text_from_socket(client_sock, constants.FILE_NAME_LEN)
        res['content'] = su.read_bytes_from_socket(client_sock, content_size)

        return res
