import socket

class RegisterMessageHandler:
    def handle_message(self, message: dict, client_sock: socket.socket) -> None:
        print(message['name'], 'wants to register!')