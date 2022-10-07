from response_serializers.response_serializer import ResponseSerializer

class RegisterResponseSerializer(ResponseSerializer):
    def serialize_response(self, response: dict) -> bytes:
        return response['id']
