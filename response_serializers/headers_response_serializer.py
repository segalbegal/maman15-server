from response_serializers.response_serializer import ResponseSerializer
from utilities.bytes_utils import BytesUtils as bu
from constants import system_constants, sizes


class HeadersResponseSerializer(ResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        buffer: bytes = bu.write_number_to_buffer(system_constants.VERSION, sizes.VERSION_LEN)
        buffer += bu.write_number_to_buffer(response['status'], sizes.STATUS_LEN)

        return buffer
