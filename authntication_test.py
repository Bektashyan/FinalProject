import encode_decode

a = encode_decode.base64_encode("Taron_2000")

b = encode_decode.base64_decode('VGFyb25fMjAwMA==')
if a == b:
    print("test successful")
else:
    print("test not successful")
