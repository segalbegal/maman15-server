from socket import socket

class SocketUtils:
    def read_text_from_socket(sock: socket, len: int, encoding='utf-8') -> str:
        text = sock.recv(len).decode(encoding)
        null_terminator_idx = text.find('\x00')
        if (null_terminator_idx > 0):
            text = text[:null_terminator_idx]
        return text

    def read_number_from_socket(sock: socket, len: int, encoding='utf-8') -> int:
        return int(SocketUtils.read_text_from_socket(sock, len, encoding))