from socket import socket

class SocketReader:
    def read_bytes_from_socket(self, sock: socket) -> bytes:
        raise NotImplementedError()
