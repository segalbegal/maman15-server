from client_handlers.client_handler import ClientHandler
from client_handlers.client_handler_resolver import ClientHandlerResolver
from client_handlers.send_file_client_handler import SendFileClientHandler
from data.ram_data_holder import RAMDataHolder
from data.sqlite_data_holder import SqliteDataHolder
from data.data_holder_composite import DataHolderComposite

from server import Server
from client_handlers.regular_client_handler import RegularClientHandler
# Message parsers
from message_parsers.register_message_parser import RegisterMessageParser
from message_parsers.message_parser_resolver import MessageParserResolver
from message_parsers.headers_message_parser import HeaderMessageParser
from message_parsers.public_key_message_parser import PublicKeyMessageParser
from message_parsers.send_file_message_parser import SendFileMessageParser
# Message handlers
from message_handlers.register_message_handler import RegisterMessageHandler
from message_handlers.message_handler_resolver import MessageHandlerResolver
from message_handlers.public_key_message_handler import PublicKeyMessageHandler
from message_handlers.send_file_message_handler import SendFileMessageHandler
# Response serializers
from response_serializers.register_response_serializer import RegisterResponseSerializer
from response_serializers.response_serializer_resolver import ResponseSerializerResolver
from response_serializers.headers_response_serializer import HeadersResponseSerializer
from response_serializers.dummy_response_serializer import DummyResponseSerialize
from response_serializers.public_key_response_serializer import PublicKeyResponseSerializer
from response_serializers.send_file_response_serializer import SendFileResponseSerializer

import constants

PORT_FILE = 'port.info'
LISTENING_IP = '127.0.0.1'

def read_listening_port() -> int:
    with open(PORT_FILE) as f:
        return int(f.readline())

def create_handler() -> ClientHandler:
    parser = MessageParserResolver(HeaderMessageParser(), {
        constants.REGISTER_MSGCODE: RegisterMessageParser(),
        constants.PUBLIC_KEY_MSGCODE: PublicKeyMessageParser(),
        constants.SEND_FILE_MSGCODE: SendFileMessageParser(),
    })

    sql_data = SqliteDataHolder()
    clients, files = sql_data.fetch_all_data()
    data_holder = DataHolderComposite([RAMDataHolder(clients, files), sql_data])
    handler = MessageHandlerResolver({
        constants.REGISTER_MSGCODE: RegisterMessageHandler(data_holder),
        constants.PUBLIC_KEY_MSGCODE: PublicKeyMessageHandler(data_holder),
        constants.SEND_FILE_MSGCODE: SendFileMessageHandler(data_holder),
    })

    serializer = ResponseSerializerResolver(HeadersResponseSerializer(), {
        constants.REGISTER_SUCC_STATUS: RegisterResponseSerializer(),
        constants.REGISTER_FAIL_STATUS: DummyResponseSerialize(),
        constants.PUBLIC_KEY_STATUS: PublicKeyResponseSerializer(),
        constants.SEND_FILE_STATUS: SendFileResponseSerializer(),
    })

    regular_client_handler = RegularClientHandler(parser, handler, serializer)
    send_file_client_handler = SendFileClientHandler(parser, handler, serializer, data_holder)

    return ClientHandlerResolver(
        parser,
        {constants.SEND_FILE_MSGCODE: send_file_client_handler,},
        regular_client_handler)

def main():
    port = read_listening_port()
    client_handler: ClientHandler = create_handler()
    server = Server(LISTENING_IP, port, client_handler)
    server.start()

if __name__ == '__main__':
    main()
