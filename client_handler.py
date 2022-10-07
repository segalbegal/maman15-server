import socket
from message_parsers.message_parser import MessageParser
from message_handlers.message_handler import MessageHandler
from response_serializers.response_serializer import ResponseSerializer

class ClientHandler:
    def __init__(self, parser: MessageParser, message_handler: MessageHandler, response_serializer: ResponseSerializer) -> None:
        self.message_parser: MessageParser = parser
        self.message_handler: MessageHandler = message_handler
        self.response_serializer = response_serializer

    def handle_client(self, client_sock: socket.socket) -> None:
        parsed_message = self.message_parser.parse_message(client_sock)
        response = self.message_handler.handle_message(parsed_message)
        serialized_response = self.response_serializer.serialize_response(response)

        print(response)
        print(serialized_response)

        client_sock.send(serialized_response)
