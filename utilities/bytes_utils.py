BYTE_BASE: int = 256

class BytesUtils:
    def write_number_to_buffer(num: int, length: int) -> bytes:
        return num.to_bytes(length, 'big')

    def write_string_to_buffer(string: str, length: int) -> bytes:
        string = string.ljust(length)
        return string.encode('utf-8')

    def subbuf(buffer: bytes, start_idx: int, length: int):
        return buffer[start_idx: start_idx + length]

    def extract_num_from_buffer(buffer: bytes, length: int, offset: int = 0):
        num: int = 0
        for i in range(length):
            num += buffer[offset + length - i - 1] * int(pow(BYTE_BASE, i))

        return num

    def extract_text_from_buffer(buffer: bytes, length: int, offset: int = 0, encoding: str = 'utf-8'):
        return BytesUtils.subbuf(buffer, offset, length).rstrip(b'\x00').decode(encoding)
