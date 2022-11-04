import socket
from client_handlers.client_handler import ClientHandler
from data.data_holder import DataHolder
from message_handlers.message_handler import MessageHandler
from message_parsers.message_parser import MessageParser
from response_serializers.response_serializer import ResponseSerializer
from socket_readers.socket_reader import SocketReader
from utilities.socket_utils import SocketUtils as su
from constants import statuses, system_constants, msg_codes

import logging
logger = logging.getLogger()

class SendFileClientHandler(ClientHandler):
    def __init__(self,
                 reader: SocketReader,
                 parser: MessageParser,
                 message_handler: MessageHandler,
                 response_serializer: ResponseSerializer,
                 data: DataHolder) -> None:
        self.socket_reader: SocketReader = reader
        self.message_parser: MessageParser = parser
        self.message_handler: MessageHandler = message_handler
        self.response_serializer = response_serializer
        self.data: DataHolder = data

    def __extract_message_from_socket(self, sock: socket.socket):
        serialized_message = self.socket_reader.read_bytes_from_socket(sock)
        return self.message_parser.parse_message(serialized_message)

    def __process_request(self, message: dict, sock: socket.socket):
        logger.debug('Received message with MessageCode: ' + str(message['msg-code']))
        response = self.message_handler.handle_message(message)
        logger.debug('Sending message with Status: ' + str(response['status']))
        serialized_response = self.response_serializer.serialize_response(response)
        su.send_bytes_to_sock(sock, serialized_response)

    def __create_accept_response(self, message: dict):
        accept_response = {
            'status': statuses.MESSAGE_APPROVED_STATUS,
            'version': system_constants.VERSION,
            'id': message['id'],
        }
        return self.response_serializer.serialize_response(accept_response)

    def handle_client(self, client_sock: socket.socket, parsed_message: dict = None) -> None:
        if parsed_message is None:
            parsed_message = self.__extract_message_from_socket(client_sock)

        self.__process_request(parsed_message, client_sock)
        serialized_accept_response = self.__create_accept_response(parsed_message)

        ack = {'msg-code': msg_codes.INVALID_CRC_RETRY_MSGCODE}
        while ack['msg-code'] == msg_codes.INVALID_CRC_RETRY_MSGCODE:
            ack = self.__extract_message_from_socket(client_sock)
            su.send_bytes_to_sock(client_sock, serialized_accept_response)
            if ack['msg-code'] == msg_codes.INVALID_CRC_RETRY_MSGCODE:
                parsed_message = self.__extract_message_from_socket(client_sock)
                self.__process_request(parsed_message, client_sock)

        if ack['msg-code'] == msg_codes.INVALID_CRC_MSGCODE:
            logger.error('Error while comparing CRC with client!')
        else:
            parsed_message['verified'] = True
            self.data.update_file_verification(parsed_message)
