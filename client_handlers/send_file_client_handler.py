import socket
from client_handlers.client_handler import ClientHandler
from data.data_holder import DataHolder
from message_handlers.message_handler import MessageHandler
from message_parsers.message_parser import MessageParser
from response_serializers.response_serializer import ResponseSerializer
from utilities.socket_utils import SocketUtils as su
import constants

class SendFileClientHandler(ClientHandler):
    def __init__(self,
                 parser: MessageParser,
                 message_handler: MessageHandler,
                 response_serializer: ResponseSerializer,
                 data: DataHolder) -> None:
        self.message_parser: MessageParser = parser
        self.message_handler: MessageHandler = message_handler
        self.response_serializer = response_serializer
        self.data: DataHolder = data

    def handle_client(self, client_sock: socket.socket, parsed_message: dict = None) -> None:
        if parsed_message is None:
            parsed_message = self.message_parser.parse_message(client_sock)

        print('Received message with MessageCode:', parsed_message['msg-code'])
        response = self.message_handler.handle_message(parsed_message)
        print('Sending message with Status:', response['status'])
        serialized_response = self.response_serializer.serialize_response(response)
        su.send_bytes_to_sock(client_sock, serialized_response)

        accept_response = {
            'status': constants.MESSAGE_APPROVED_STATUS,
            'version': constants.VERSION,
            'id': parsed_message['id'],
        }
        serialized_accept_response = self.response_serializer.serialize_response(accept_response)

        ack = {'msg-code': constants.INVALID_CRC_RETRY_MSGCODE}
        while ack['msg-code'] == constants.INVALID_CRC_RETRY_MSGCODE:
            ack = self.message_parser.parse_message(client_sock)
            su.send_bytes_to_sock(client_sock, serialized_accept_response)
            if ack['msg-code'] == constants.INVALID_CRC_RETRY_MSGCODE:
                parsed_message = self.message_parser.parse_message(client_sock)
                print('Received message with MessageCode:', parsed_message['msg-code'])
                response = self.message_handler.handle_message(parsed_message)
                print('Sending response with Status:', response['status'])
                serialized_response = self.response_serializer.serialize_response(response)
                su.send_bytes_to_sock(client_sock, serialized_response)

        if ack['msg-code'] == constants.INVALID_CRC_MSGCODE:
            print('Error while comparing CRC with client!')
        else:
            parsed_message['verified'] = True
            self.data.update_file_verification(parsed_message)

        client_sock.close()
