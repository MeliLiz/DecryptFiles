# Decrypts the encrypted file
def decrypt(file):
    key = 0x0
    for i in range(0x100): # This is the key space
        key = i # The key is the current value of i
        file.seek(0)
        data = file.read() 
        decrypted = ""
        for byte in data:
            decrypted += chr(byte ^ key)
        if "flag" in decrypted:
            print(f"Key: {key}")
            print(decrypted)
            break
    return decrypted

# decrypt a file using congruences
def decrypt(file):
    data = file.read()
    numbers = [x for x in data] # bytes as integers
    
    for i in range(256):
        for j in range(256):
            numbers[i] = numbers[i] * i + j

    decrypted = "".join([chr(x) for x in numbers])
    return decrypted



if "__main__" == __name__:
    file_signatures = {'png': b'\x89PNG\r\n\x1a\n', 'jpg': b'\xff\xd8\xff\xe0\x00\x10JFIF', 'pdf': b'%PDF-', 'zip': b'PK\x03\x04'}
    #file_signatures1 = {'png': [89, 50, 4e, 47, 0d, 0a, 1a, 0a], 'pdf': [25, 50, 44, 46, 2D], 'mp3': [49, 44, 33], 'mp3_1': [FF], 'mp4': [66, 74, 79 70]}
    file_signatures1 = {
                        'png': [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a], 
                        'pdf': [0x25, 0x50, 0x44, 0x46, 0x2D], 
                        'mp3': [0x49, 0x44, 0x33], 
                        'mp3_1': [0xFF], 
                        'mp4': [0x66, 0x74, 0x79, 0x70]
                    }
    file = open("file1.lol", "rb")
    data = file.read()
    #print(data[:100])
    numbers = [x for x in data] # bytes as integers
    hexa = " ".join([hex(x) for x in numbers ])
    # prinnt the numbers in hex
    #print(hexa[:100])

    """for i in range(256):
        for j in range(256):
            numbers[i] = numbers[i] * i + j"""

    """ decrypted = decrypt(file)
    with open("decrypted.txt", "w") as f:
        f.write(decrypted)
    file.close()"""
