from response_serializers.response_serializer import ResponseSerializer

class PublicKeyResponseSerializer(ResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        return response['id'] + response['aes-key']
