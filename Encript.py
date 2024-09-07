from encriptFiles import affine_encrypt_file, base64_encode_file
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 Main.py <input_file> <output_file> <alpha> [-b] ")
        print("     -b to encode in base64")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]


        if len(sys.argv) == 4 and sys.argv[3] == "-b":
            print("Codificando en base64")
            base64_encode_file(input_file, output_file)
            sys.exit(0)
        else:
            a = int(sys.argv[3])


    print("Encriptando archivo con funciones afines")
    affine_encrypt_file(input_file, output_file, a)
    print("Archivo encriptado guardado como: ", output_file)
