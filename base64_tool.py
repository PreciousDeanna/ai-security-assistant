import base64

def encode_string(input_str):
    """
    Encodes the input string to Base64.
    """
    encoded_bytes = base64.b64encode(input_str.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_string(encoded_str):
    """
    Decodes a Base64 encoded string.
    """
    try:
        decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"[ERROR] Invalid Base64 input: {str(e)}"
