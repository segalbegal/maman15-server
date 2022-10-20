import socket

class ClientHandler:
    def handle_client(self, client_sock: socket.socket, message: dict = None) -> None:
        raise NotImplementedError()
