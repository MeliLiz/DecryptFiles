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

def save_as_png(bytes_array, output_file):
    # Escribe los bytes en un archivo PNG
    with open(output_file, 'wb') as f:
        f.write(bytearray(bytes_array))

if __name__ == "__main__":
    # Leer archivo base64
    with open("file1.lol", "r") as f:
        base64_data = f.read()
    
    # Decodificar base64 a bytes
    img_bytes = base64_to_bytes(base64_data)
    
    # Guardar como imagen PNG
    save_as_png(img_bytes, "decrypted_img.png")