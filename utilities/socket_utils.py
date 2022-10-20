from socket import socket
from math import pow
from utilities.bytes_utils import BytesUtils as bu

BYTE_BASE = 256

class SocketUtils:
    def read_bytes_from_socket(sock: socket, length: int):
        return sock.recv(length)

    def read_text_from_socket(sock: socket, length: int, encoding: str = 'utf-8') -> str:
        text = SocketUtils.read_bytes_from_socket(sock, length).decode(encoding)
        null_terminator_idx = text.find('\x00')
        if null_terminator_idx > 0:
            text = text[:null_terminator_idx]
        return text

    def read_number_from_socket(sock: socket, length: int) -> int:
        buffer = SocketUtils.read_bytes_from_socket(sock, length)
        num: int = 0
        for i in range(length):
            num += buffer[length - i - 1] * int(pow(BYTE_BASE, i))

        return num

    def send_bytes_to_sock(sock: socket, data: bytes):
        sock.send(data)

    def send_text_to_sock(sock: socket, data: str, encoding: str = 'utf-8'):
        SocketUtils.send_bytes_to_sock(sock, data.encode(encoding))

    def send_number_to_sock(sock: socket, num: int, length: int):
        buffer = bu.write_number_to_buffer(num, length)
        SocketUtils.send_bytes_to_sock(sock, buffer)
