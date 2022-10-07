from data.data_holder import DataHolder

class DataHolderComposite(DataHolder):
    def __init__(self, holders: list):
        self.holders: list = holders

    def update_last_seen(self, id: bytes) -> None:
        for holder in self.holders:
            holder.update_last_seen(id)

    def user_exists(self, name: str) -> bool:
        return self.holders[0].user_exists(name)

    def insert_user(self, details: dict) -> None:
        for holder in self.holders:
            holder.insert_user(details)

    def update_user_cred(self, details: dict) -> None:
        for holder in self.holders:
            holder.update_user_cred(details)

    def insert_file(self, details: dict) -> None:
        for holder in self.holders:
            holder.insert_file(details)