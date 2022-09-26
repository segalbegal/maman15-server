from server import Server
from client_handler import ClientHandler

PORT_FILE = 'port.info'
LISTENING_IP = '127.0.0.1'

def read_listening_port():
    with open(PORT_FILE) as f:
        return int(f.readline())

def main():
    port = read_listening_port()
    server = Server(LISTENING_IP, port, ClientHandler())
    server.start()

if __name__ == '__main__':
    main()