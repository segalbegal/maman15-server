from server import Server
from client_handler import ClientHandler
import message_parsers.register_message_parser as register_parser
import message_handlers.register_message_handler as register_handlers
import constants

PORT_FILE = 'port.info'
LISTENING_IP = '127.0.0.1'

def read_listening_port() -> int:
    with open(PORT_FILE) as f:
        return int(f.readline())

def create_handler() -> ClientHandler:
    parsers = {
        constants.REGISTER_MSGCODE: register_parser.RegisterMessageParser(),
    }
    handlers = {
        constants.REGISTER_MSGCODE: register_handlers.RegisterMessageHandler(),
    }
    return ClientHandler(parsers, handlers)

def main():
    port = read_listening_port()
    client_handler: ClientHandler = create_handler()
    server = Server(LISTENING_IP, port, client_handler)
    server.start()

if __name__ == '__main__':
    main()