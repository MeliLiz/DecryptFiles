import os
import random

def affine_encrypt(byte, a, b):
    return (a*byte + b) % 256

def encode_base64(data):
    BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # Convert the data to a binary string
    binary_str = ''.join(f'{byte:08b}' for byte in data)
    
    # Make the binary string a multiple of 6
    extraBits = (6 - len(binary_str) % 6)
    extraBits = extraBits%6 # If the length is already a multiple of 6.
    binary_str = binary_str + '0' * extraBits
    
    # Encode the binary string in Base64 by grouping 6 bits at a time (2^6)
    encoded_str = ''
    for i in range(0, len(binary_str), 6):
        six_bits = binary_str[i:i+6]
        index = int(six_bits, 2)
        encoded_str += BASE64_CHARS[index]
    if extraBits > 0:
         encoded_str += '=' * (extraBits // 2)
    
    return encoded_str

def affine_encrypt_file(file_path,otput_name):
    b = random.randint(0, 255)
    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = bytes([affine_encrypt(x, 83, b) for x in data])

    with open(otput_name, "wb") as f:
        f.write(encrypted_data)
    
def base64_encode_file(file_path, output_name):
    with open(file_path, "rb") as f:
        data = f.read()
    
    base64_encoded_data = encode_base64(data)

    with open(output_name, "w") as f:
        f.write(base64_encoded_data)
