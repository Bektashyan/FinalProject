import base64


def base64_encode(text):
    # Encode the text to bytes and then encode using base64
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    # Convert the bytes to a string
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text


def base64_decode(encoded_text):
    # Decode the base64 encoded text to bytes
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    # Convert the bytes to a string
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text
