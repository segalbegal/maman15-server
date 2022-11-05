from socket import socket
from socket_readers.socket_reader import SocketReader
from utilities.socket_utils import SocketUtils as su
from utilities.bytes_utils import BytesUtils as bu
from constants import sizes

class BasicSocketReader(SocketReader):
    def read_bytes_from_socket(self, sock: socket) -> bytes:
        headers = su.read_bytes_from_socket(sock, sizes.HEADERS_LEN - sizes.PAYLOAD_SIZE_LEN)
        payload_len_buf = su.read_bytes_from_socket(sock, sizes.PAYLOAD_SIZE_LEN)
        payload_len = bu.extract_num_from_buffer(payload_len_buf, len(payload_len_buf))

        headers += payload_len_buf
        headers += su.read_bytes_from_socket(sock, payload_len)

        return headers
