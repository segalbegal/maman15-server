BYTE_BASE: int = 256

class BytesUtils:
    def write_number_to_buffer(num: int, length: int) -> bytes:
        return num.to_bytes(length, 'big')

    def write_string_to_buffer(string: str, length: int) -> bytes:
        string = string.ljust(length)
        return string.encode('utf-8')
