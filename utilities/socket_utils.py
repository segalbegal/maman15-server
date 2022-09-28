from socket import socket
from math import pow
from bytes_utils import BytesUtils as bu

BYTE_BASE = 256

class SocketUtils:
    def read_bytes_from_socket(sock: socket, len: int):
        return sock.recv(len)

    def read_text_from_socket(sock: socket, len: int, encoding='utf-8') -> str:
        text = SocketUtils.read_bytes_from_socket(sock, len).decode(encoding)
        null_terminator_idx = text.find('\x00')
        if (null_terminator_idx > 0):
            text = text[:null_terminator_idx]
        return text

    def read_number_from_socket(sock: socket, len: int, encoding: str='utf-8') -> int:
        buffer = SocketUtils.read_bytes_from_socket(sock, len)
        num: int = 0
        for i in range(len):
            num += buffer[len - i - 1] * int(pow(BYTE_BASE, i))

        return num

    def send_bytes_to_sock(sock: socket, data):
        sock.send(data)

    def send_text_to_sock(sock: socket, data: str, encoding: str='utf-8'):
        SocketUtils.send_bytes_to_sock(sock, data.encode(encoding))

    def send_number_to_sock(sock: socket, num: int, len: int, encoding: str='utf-8'):
        buffer = bu.write_number_to_buffer(num, len)
        SocketUtils.send_bytes_to_sock(sock, buffer)