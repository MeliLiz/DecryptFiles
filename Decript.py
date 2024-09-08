import sys
def decode_mod(file_path, decrypted_name):
    #Colors for the output
    BLUE = '\033[94m'
    ENDC = '\033[0m'

    file_signatures1 = {'png': [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a], 
                        'pdf': [0x25, 0x50, 0x44, 0x46, 0x2D], 
                        'mp3': [0x49, 0x44, 0x33], 
                        'mp4': [0x66, 0x74, 0x79, 0x70],
                        'jpg': [0xFF, 0xD8, 0xFF, 0xE0],
                        'jpeg': [0xFF, 0xD8, 0xFF, 0xE0]}
    
    file = open(file_path, "rb")
    data = file.read()
    numbers = [x for x in data] # bytes as integers
    hexadecimal = [hex(x) for x in numbers ] # bytes as hexadecimal

    #Transform the hexadecimal numbers to decimal
    decimal_file = [int(x, 16) for x in hexadecimal]
    print("Decimal file: ", decimal_file[:10])

    #Transform the file signatures1 to decimal
    decimal_signatures = {}
    for key in file_signatures1:
        decimal_signatures[key] = [int(x) for x in file_signatures1[key]]

    for key in decimal_signatures:
        #Make the ecuation system to find alpha and beta
        print(BLUE, "KEY: ", key, ENDC)
        if key == 'mp4': #If its an mp4, we need to start from the fifth byte
            first_file = decimal_file[5] # First byte of the file
            second_file = decimal_file[6] # Second byte of the file
            first_sign = decimal_signatures[key][1]  # First byte of the signature
            second_sign = decimal_signatures[key][2]  
            print("First file: ", first_file, "Second file: ", second_file)
        else:
            first_file = decimal_file[0] # First byte of the file
            second_file = decimal_file[1] # Second byte of the file
            first_sign = decimal_signatures[key][0]  # First byte of the signature
            second_sign = decimal_signatures[key][1]  # Second byte of the signature

        alpha_mult = (first_file - second_file) % 256 
        right_side = (first_sign - second_sign) % 256

        print("Tryingf: (", first_file," - ", second_file, ") a = (", first_sign, " - ", second_sign, ") mod 256")
        print("Tryingf:", alpha_mult, "a = " , right_side, "mod 256")

        inverses_alpha_mult = [x for x in range(256) if (x * alpha_mult) % 256 == 1] # Get the inverses of alpha_mult

        # If we are not working with something that has inverse, then we need to change the order of the ecuation
        if len(inverses_alpha_mult) == 0: 

            alpha_mult = (first_sign - second_sign) % 256
            right_side = (first_file - second_file) % 256

            inverses_alpha_mult = [x for x in range(256) if (x * alpha_mult) % 256 == 1] # Get the inverses of alpha_mult

            print("Trying: (", first_sign," - ", second_sign, ") a = (", first_file, " - ", second_file, " = " , right_side, ") mod 256")
            print("Trying: ", alpha_mult, "a = " , right_side, "mod 256")
            #print("Inverses: ", inverses_alpha_mult)

            if inverses_alpha_mult == []:
                print("No tiene inverso")
                continue
            else:
                alpha = right_side * inverses_alpha_mult[0] % 256
                beta = (first_file - (first_sign * alpha)) % 256

        else:
            alpha = right_side * inverses_alpha_mult[0] % 256
            beta = (first_sign - (first_file * alpha)) % 256

        # Apply the operations to each byte of the file
        decoded = []
        for i,num in enumerate(decimal_file):
            decoded.append((num * alpha + beta) % 256)

        print("Decoded: ", decoded[:10])

        # Check if the fist bytes are the same as the signature
        signature = file_signatures1[key]
        decimal_file_signature = decoded[:len(signature)]
        print("Sign: ", signature)

        found = True
        if key == 'mp4':
            for i in range(4, len(signature)):
                if decimal_file_signature[i] != signature[i]:
                    found = False
                    break
        else:
            for i in range(len(signature)):
                if decimal_file_signature[i] != signature[i]:
                    found = False
                    break

        # Write the file
        if found:
            file = open(decrypted_name +"." + key, "wb")
            file.write(bytearray(decoded))
            file.close()
            break

    return found



if "__main__" == __name__:
    if len(sys.argv) < 3:
        print("Usage: python3 Main.py <input_file> <output_file>")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print(decode_mod(input_file, output_file))
    
    #print(decode_mod("file4.lol", "File4_decoded"))


    
