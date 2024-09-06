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
    file = open("file1.lol", "rb")
    data = file.read()
    numbers = [x for x in data] # bytes as integers
    hexa = " ".join([hex(x) for x in numbers ])
    # prinnt the numbers in hex
    print(hexa[:100])

    for i in range(256):
        for j in range(256):
            numbers[i] = numbers[i] * i + j

    """ decrypted = decrypt(file)
    with open("decrypted.txt", "w") as f:
        f.write(decrypted)
    file.close()"""
