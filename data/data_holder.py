class DataHolder:
    def update_last_seen(self, id) -> None:
        raise NotImplementedError()

    def user_exists(self, name: str) -> bool:
        raise NotImplementedError()

    def insert_user(self, details: dict) -> None:
        raise NotImplementedError()

    def update_user(self, details: dict) -> None:
        self.update_last_seen(details['id'])
        raise NotImplementedError()

    def insert_file(self, details: dict) -> None:
        self.update_last_seen(details['id'])
        raise NotImplementedError()