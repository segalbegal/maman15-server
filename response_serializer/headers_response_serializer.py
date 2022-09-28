from response_serializer import ResponseSerializer
from utilities.bytes_utils import BytesUtils as bu
import constants

class HeadersResponseSerializer(ResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        buffer: bytes = bu.write_number_to_buffer(constants.VERSION, constants.VERSION_LEN)
        buffer += bu.write_number_to_buffer(response['status'], constants.STATUS_LEN)
        buffer += bu.write_number_to_buffer(response['payload-size'], constants.PAYLOAD_SIZE_LEN)

        return buffer;