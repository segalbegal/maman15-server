from data.ram_data_holder import RAMDataHolder
from data.sqlite_data_holder import SqliteDataHolder
from data.data_holder_composite import DataHolderComposite

from server import Server
from client_handler import ClientHandler
# Message parsers
from message_parsers.register_message_parser import RegisterMessageParser
from message_parsers.message_parser_resolver import MessageParserResolver
from message_parsers.headers_message_parser import HeaderMessageParser
# Message handlers
from message_handlers.register_message_handler import RegisterMessageHandler
from message_handlers.message_handler_resolver import MessageHandlerResolver
# Response serializers
from response_serializers.register_response_serializer import RegisterResponseSerializer
from response_serializers.response_serializer_resolver import ResponseSerializerResolver
from response_serializers.headers_response_serializer import HeadersResponseSerializer
from response_serializers.dummy_response_serializer import DummyResponseSerialize

import constants

PORT_FILE = 'port.info'
LISTENING_IP = '127.0.0.1'

def read_listening_port() -> int:
    with open(PORT_FILE) as f:
        return int(f.readline())

def create_handler() -> ClientHandler:
    parser = MessageParserResolver(HeaderMessageParser(), {
        constants.REGISTER_MSGCODE: RegisterMessageParser(),
    })

    sql_data = SqliteDataHolder()
    clients, files = sql_data.fetch_all_data()
    data_holder = DataHolderComposite([RAMDataHolder(clients, files), sql_data])
    handler = MessageHandlerResolver({
        constants.REGISTER_MSGCODE: RegisterMessageHandler(data_holder),
    })

    serializer = ResponseSerializerResolver(HeadersResponseSerializer(), {
        constants.REGISTER_SUCC_STATUS: RegisterResponseSerializer(),
        constants.REGISTER_FAIL_STATUS: DummyResponseSerialize(),
    })

    return ClientHandler(parser, handler, serializer)

def main():
    port = read_listening_port()
    client_handler: ClientHandler = create_handler()
    server = Server(LISTENING_IP, port, client_handler)
    server.start()

if __name__ == '__main__':
    main()
