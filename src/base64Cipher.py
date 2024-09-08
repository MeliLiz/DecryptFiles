import sys

# String de valores base64
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# Diccionario de "file signatures" con las extensiones correspondientes
file_signatures1 = {
    'png': [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a],
    'pdf': [0x25, 0x50, 0x44, 0x46, 0x2D],
    'mp3': [0x49, 0x44, 0x33],
    'mp4': [0x66, 0x74, 0x79, 0x70],
    'jpg': [0xFF, 0xD8, 0xFF, 0xE0],
    'jpeg': [0xFF, 0xD8, 0xFF, 0xE0]
}

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

def detect_extension(bytes_array):
    # Toma los primeros bytes para compararlos con las firmas de archivos
    for extension, signature in file_signatures1.items():
        if bytes_array[:len(signature)] == signature:
            return '.' + extension
    return '.bin'  # Si no se detecta, guarda como archivo binario genérico

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 base64Cipher.py <input_file> <output_file_base>")
        sys.exit(1)
    else: 
        input_file = sys.argv[1]
        output_file_base = sys.argv[2]
        
        # Leer el archivo base64
        with open(input_file, "r") as f:
            base64_data = f.read()
        
        # Decodificar base64 a bytes
        img_bytes = base64_to_bytes(base64_data)
        
        # Detectar la extensión del archivo
        file_extension = detect_extension(img_bytes)
        
        # Generar el nombre completo del archivo de salida con la extensión
        output_file = output_file_base + file_extension
        
        # Guardar el archivo decodificado
        save(img_bytes, output_file)
        print(f"Archivo guardado como: {output_file}")
