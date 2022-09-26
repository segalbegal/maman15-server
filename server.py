import socket
import threading

class Server:
    def __init__(self, ip, port, client_handler):
        self.ip = ip
        self.port = port
        self.client_handler = client_handler

    def start(self):
        listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_sock.bind((self.ip, self.port))
        listen_sock.listen()

        self.running = True
        while self.running:
            client_sock, addr = listen_sock.accept()
            threading.Thread(target=self.client_handler.handle_client, args=(client_sock,)).start()

    def stop(self):
        self.running = False