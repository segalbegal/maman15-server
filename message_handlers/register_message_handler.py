from socket import socket
from data.data_holder import DataHolder
from constants import REGISTER_SUCC_STATUS, REGISTER_FAIL_STATUS, NAME_LEN
from utilities.socket_utils import SocketUtils as su
import uuid

class RegisterMessageHandler:
    def __init__(self, data: DataHolder):
        self.data: DataHolder = data

    def handle_message(self, message: dict, client_sock: socket) -> None:
        if self.data.user_exists(message['name']):
            RegisterMessageHandler.handle_user_exists(message, client_sock)
            return

        message['id'] = uuid.uuid1().bytes
        self.data.insert_user(message)



    def handle_user_exists(message: dict, client_sock: socket):
        padded_name = message['name'].ljust(NAME_LEN, '\x00')
        su.send_number_to_sock(client_sock, REGISTER_FAIL_STATUS)
        su.send_text_to_sock(client_sock, padded_name)