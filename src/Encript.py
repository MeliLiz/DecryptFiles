from encriptFiles import affine_encrypt_file, base64_encode_file
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 Main.py <input_file> <output_file> <alpha>")
        print("     -b to encode in base64")
        sys.exit(1)
    else:
        b64 = False
        inFle = False
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "-b":
                b64 = True
                continue
            if not inFle:
                inFle = True
                input_file = sys.argv[i]
                continue
            output_file = sys.argv[i]
            break
                

        if b64:
            print("Codificando en base64")
            base64_encode_file(input_file, output_file)
            sys.exit(0)
        a = int(sys.argv[3])

    print("Encriptando archivo con funciones afines")
    affine_encrypt_file(input_file, output_file, a)
    print("Archivo encriptado guardado como: ", output_file)
