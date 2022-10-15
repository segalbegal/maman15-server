from response_serializers.response_serializer import ResponseSerializer
from utilities.bytes_utils import BytesUtils as bu
import constants

class SendFileResponseSerializer(ResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        buffer = response['id']
        buffer += bu.write_number_to_buffer(response['content-size'], constants.FILE_SIZE_LEN)
        buffer += bu.write_string_to_buffer(response['file-name'], constants.FILE_NAME_LEN)
        buffer += bu.write_number_to_buffer(response['cksum'], constants.CKSUM_KEN)

        return buffer
