class DataHolder:
    def update_last_seen(self, id: bytes) -> None:
        raise NotImplementedError()

    def user_exists(self, name: str) -> bool:
        raise NotImplementedError()

    def insert_user(self, details: dict) -> None:
        raise NotImplementedError()

    def update_user_cred(self, details: dict) -> None:
        raise NotImplementedError()

    def insert_file(self, details: dict) -> None:
        raise NotImplementedError()

    def update_file_verification(self, details: dict) -> None:
        raise NotImplementedError()

    def get_user_name(self, details: dict) -> str:
        raise NotImplementedError()

    def get_user_aes(self, details: dict) -> bytes:
        raise NotImplementedError()
