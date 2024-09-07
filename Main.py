from encryptFiles import affine_encrypt_file, base64_encode_file
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 Main.py <input_file> <output_file> [-b]")
        print("     -b to encode in base64")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        if len(sys.argv) == 4 and sys.argv == "-b":
            base64_encode_file(input_file, output_file)
            sys.exit(0)
    affine_encrypt_file(input_file, output_file)
    base64_encode_file(input_file, output_file)