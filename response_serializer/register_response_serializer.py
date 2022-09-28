from headers_response_serializer import HeadersResponseSerializer
from utilities.bytes_utils import BytesUtils as bu

class RegisterResponseSerializer(HeadersResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        buffer = super().serialize_response(response)
        buffer += bu.