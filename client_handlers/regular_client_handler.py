import socket
from client_handlers.client_handler import ClientHandler
from message_parsers.message_parser import MessageParser
from message_handlers.message_handler import MessageHandler
from response_serializers.response_serializer import ResponseSerializer
from utilities.socket_utils import SocketUtils as su

class RegularClientHandler(ClientHandler):
    def __init__(self, parser: MessageParser, message_handler: MessageHandler, response_serializer: ResponseSerializer) -> None:
        self.message_parser: MessageParser = parser
        self.message_handler: MessageHandler = message_handler
        self.response_serializer = response_serializer

    def handle_client(self, client_sock: socket.socket, parsed_message: dict = None) -> None:
        if parsed_message is None:
            parsed_message = self.message_parser.parse_message(client_sock)

        print('Received message with MessageCode:', parsed_message['msg-code'])
        response = self.message_handler.handle_message(parsed_message)
        print('Sending message with Status:', response['status'])
        serialized_response = self.response_serializer.serialize_response(response)
        su.send_bytes_to_sock(client_sock, serialized_response)
