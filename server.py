import socket
import threading
from client_handlers.client_handler import ClientHandler
import logging
logger = logging.getLogger()

class Server:
    def __init__(self, ip: str, port: int, client_handler: ClientHandler) -> None:
        self.ip: str = ip
        self.port: int = port
        self.client_handler: ClientHandler = client_handler
        self.running: bool = False

    def __process_client(self, client_sock: socket.socket):
        self.client_handler.handle_client(client_sock)
        client_sock.close()

    def start(self) -> None:
        logger.info(f'Starting to listen at Ip: {self.ip}, Port: {self.port}')
        listen_sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_sock.bind((self.ip, self.port))
        listen_sock.listen()

        self.running: bool = True
        while self.running:
            client_sock, addr = listen_sock.accept()
            logger.info(f'Client connected. ClientIp: {addr[0]}, ClientPort: {addr[1]}')
            threading.Thread(target=self.__process_client, args=(client_sock,)).start()

    def stop(self) -> None:
        self.running = False
