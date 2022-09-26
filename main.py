from data.ram_data_holder import RAMDataHolder
from data.sqlite_data_holder import SqliteDataHolder
from data.data_holder_composite import DataHolderComposite

from server import Server
from client_handler import ClientHandler
from message_parsers.register_message_parser import RegisterMessageParser
from message_handlers.register_message_handler import RegisterMessageHandler
import constants

PORT_FILE = 'port.info'
LISTENING_IP = '127.0.0.1'

def read_listening_port() -> int:
    with open(PORT_FILE) as f:
        return int(f.readline())

def create_handler() -> ClientHandler:
    parsers = {
        constants.REGISTER_MSGCODE: RegisterMessageParser(),
    }
    sql_data = SqliteDataHolder()
    clients, files = sql_data.fetch_all_data()
    data_holder = DataHolderComposite([RAMDataHolder(clients, files), sql_data])
    handlers = {
        constants.REGISTER_MSGCODE: RegisterMessageHandler(data_holder),
    }
    return ClientHandler(parsers, handlers)

def main():
    port = read_listening_port()
    client_handler: ClientHandler = create_handler()
    server = Server(LISTENING_IP, port, client_handler)
    server.start()

if __name__ == '__main__':
    main()