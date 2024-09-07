import sys

# string de valores base64
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_to_bytes(data):
    # Elimina cualquier salto de línea o espacios en blanco
    data = data.strip().replace('\n', '')
    
    binary_string = ""
    
    # Convierte cada carácter de base64 en sus 6 bits correspondientes
    for char in data:
        binary_string += format(base64_chars.index(char), '06b')
    
    # Agrupar los bits en bytes (grupos de 8)
    bytes_array = []
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            bytes_array.append(int(byte, 2))
    
    return bytes_array

def save(bytes_array, output_file):
    # Escribe los bytes en un archivo
    with open(output_file, 'wb') as f:
        f.write(bytearray(bytes_array))

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python3 base64Cipher.py <input_file>")
        sys.exit(1)
    else: 
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        with open(input_file, "r") as f:
            base64_data = f.read()
        img_bytes = base64_to_bytes(base64_data)
        save(img_bytes, output_file)
