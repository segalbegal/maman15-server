class ResponseSerializer:
    def serialize_response(self, response: dict) -> bytes:
        raise NotImplementedError()