class BytesUtils:
    def write_number_to_buffer(num: int, len: int) -> bytes:
        buffer = bytes(len)
        for i in range(len):
            buffer[len - i - 1] = num % BYTE_BASE
            num /= BYTE_BASE
        return buffer;

    def write_string_to_buffer(sting: str, len: int) -> bytes:
        str = str.ljust(len)
        return str.encode('utf-8')