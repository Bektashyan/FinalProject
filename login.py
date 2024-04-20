import encode_decode

import register


def login():
    decoded_pass = encode_decode.base64_decode(input(f'{register.Pass}'))
    if register.Pass == decoded_pass:
        print("successfully log in")
    else:
        print("The username or password was entered incorrectly")
