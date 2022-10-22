from response_serializers.response_serializer import ResponseSerializer
from utilities.bytes_utils import BytesUtils as bu
from constants import sizes

class SendFileResponseSerializer(ResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        buffer = response['id']
        buffer += bu.write_number_to_buffer(response['content-size'], sizes.FILE_SIZE_LEN)
        buffer += bu.write_string_to_buffer(response['file-name'], sizes.FILE_NAME_LEN)
        buffer += bu.write_number_to_buffer(response['cksum'], sizes.CKSUM_LEN)

        return buffer
