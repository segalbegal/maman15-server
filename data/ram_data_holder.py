import datetime
from data.data_holder import DataHolder

class RAMDataHolder(DataHolder):
    def __init__(self):
        self.clients: dict = {}
        self.client_names: list = []
        self.files: list = []

    def update_last_seen(self, id) -> None:
        self.clients[id]['last-seen'] = datetime.datetime.now()

    def user_exists(self, name: str) -> bool:
        return name in self.client_names

    def insert_user(self, details: dict) -> None:
        self.client_names.append(details['name'])
        self.clients[details['id']] = details
        self.update_last_seen(details['id'])

    def update_user(self, details: dict) -> None:
        self.clients[details['id']]['public-key'] = details['public-key']
        self.clients[details['id']]['aes-key'] = details['aes-key']

    def insert_file(self, details: dict) -> None:
        self.files.append(details)