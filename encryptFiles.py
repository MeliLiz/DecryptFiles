import os

def affine_encrypt(byte, a, b):
    return (a*byte  + b) % 256

def encrypt_file(file_path,b,otput_name):
    with open(file_path, "rb") as f:
        data = f.read()

    encrypted_data = bytes([affine_encrypt(x, 83,b ) for x in data])

    with open(otput_name, "wb") as f:
        f.write(encrypted_data)


if __name__ == "__main__":
    input_file = "./demo_files/dream_a_little_dream.mp3"
    output_file = "./demo_files/file6.jjk"

    encrypt_file(input_file, 3, output_file)

