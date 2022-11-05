from response_serializers.response_serializer import ResponseSerializer
from response_serializers.headers_response_serializer import HeadersResponseSerializer
from utilities.bytes_utils import BytesUtils as bu
from constants.sizes import PAYLOAD_SIZE_LEN

class ResponseSerializerResolver(ResponseSerializer):
    def __init__(self, headers_serializer: HeadersResponseSerializer, serializers: dict):
        self.headers_serializer = headers_serializer
        self.serializers = serializers

    def serialize_response(self, response: dict) -> bytes:
        headers = self.headers_serializer.serialize_response(response)
        if response['status'] in self.serializers:
            payload = self.serializers[response['status']].serialize_response(response)
        else:
            payload = b''
        headers += bu.write_number_to_buffer(len(payload), PAYLOAD_SIZE_LEN)
        headers += payload

        return headers
