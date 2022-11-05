from response_serializers.response_serializer import ResponseSerializer

class DummyResponseSerialize(ResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        return b''
