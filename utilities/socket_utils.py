from socket import socket

class SocketUtils:
    def read_text_from_socket(sock: socket, len: int, encoding='utf-8') -> str:
        text = sock.recv(len).decode(encoding)
        null_terminator_idx = text.find('\x00')
        if (null_terminator_idx > 0):
            text = text[:null_terminator_idx]
        return text

    def read_number_from_socket(sock: socket, len: int, encoding: str='utf-8') -> int:
        return int(SocketUtils.read_text_from_socket(sock, len, encoding))

    def send_bytes_to_sock(sock: socket, data):
        sock.send(data)

    def send_text_to_sock(sock: socket, data: str, encoding: str='utf-8'):
        SocketUtils.send_bytes_to_sock(sock, data.encode(encoding))

    def send_number_to_sock(sock: socket, num: int, encoding: str='utf-8'):
        SocketUtils.send_text_to_sock(sock, str(num), encoding)