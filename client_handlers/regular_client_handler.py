import socket
from client_handlers.client_handler import ClientHandler
from message_parsers.message_parser import MessageParser
from message_handlers.message_handler import MessageHandler
from response_serializers.response_serializer import ResponseSerializer
from socket_readers.socket_reader import SocketReader
from utilities.socket_utils import SocketUtils as su

class RegularClientHandler(ClientHandler):
    def __init__(self, socket_reader: SocketReader, message_parser: MessageParser, message_handler: MessageHandler, response_serializer: ResponseSerializer) -> None:
        self.socket_reader: SocketReader = socket_reader
        self.message_parser: MessageParser = message_parser
        self.message_handler: MessageHandler = message_handler
        self.response_serializer = response_serializer

    def handle_client(self, client_sock: socket.socket, parsed_message: dict = None) -> None:
        if parsed_message is None:
            serialized_message = self.socket_reader.read_bytes_from_socket(client_sock)
            parsed_message = self.message_parser.parse_message(serialized_message)

        print('Received message with MessageCode:', parsed_message['msg-code'])
        response = self.message_handler.handle_message(parsed_message)
        serialized_response = self.response_serializer.serialize_response(response)
        print('Sending message with Status:', response['status'])
        su.send_bytes_to_sock(client_sock, serialized_response)
