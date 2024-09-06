

if "__main__" == __name__:
    #file_signatures = {'png': b'\x89PNG\r\n\x1a\n', 'jpg': b'\xff\xd8\xff\xe0\x00\x10JFIF', 'pdf': b'%PDF-', 'zip': b'PK\x03\x04'}
    file_signatures1 = {
                        'png': [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a], 
                        'pdf': [0x25, 0x50, 0x44, 0x46, 0x2D], 
                        'mp3': [0x49, 0x44, 0x33], 
                        'mp3_1': [0xFF, 0xFB], 
                        'mp4': [0x66, 0x74, 0x79, 0x70]
                    }
    file = open("file4.lol", "rb")
    data = file.read()
    numbers = [x for x in data] # bytes as integers
    hexadecimal = [hex(x) for x in numbers ] # bytes as hexadecimal
    #print(hexadecimal[:10])

    #Transform the hexadecimal numbers to decimal
    decimal_file = [int(x, 16) for x in hexadecimal]
    #print(decimal[:10])

    #Transform the file signatures1 to decimal
    decimal_signatures = {}
    for key in file_signatures1:
        decimal_signatures[key] = [int(x) for x in file_signatures1[key]]

    #print(decimal_signatures)

    for key in decimal_signatures:
        #Make the ecuation system to find alpha and beta
        first_file = decimal_file[0] # First byte of the file
        second_file = decimal_file[1] # Second byte of the file
        first_sign = decimal_signatures[key][0]  # First byte of the signature
        second_sign = decimal_signatures[key][1]  # Second byte of the signature

        alpha_mult = (first_file - second_file) % 256 
        right_side = (first_sign - second_sign) % 256

        #print("alpha_mult: ", alpha_mult)

        inverses_alpha_mult = [x for x in range(256) if (x * alpha_mult) % 256 == 1] # Get the inverses of alpha_mult

        if len(inverses_alpha_mult) == 0: # If we are not working with something that has inverse
            alpha_mult = (first_sign - second_sign) % 256
            print("alpha_mult: ", alpha_mult % 256)
            right_side = (first_file - second_file) % 256

            inverses_alpha_mult = [x for x in range(256) if (x * alpha_mult) % 256 == 1] # Get the inverses of alpha_mult
            if inverses_alpha_mult == []:
                print("No tiene inverso")
                continue
            else:
                alpha = right_side * inverses_alpha_mult[0] % 256
                beta = (first_file - (first_sign * alpha)) % 256
                print("alpha: ", alpha)
                print("beta: ", beta)

        else:
            alpha = right_side * inverses_alpha_mult[0] % 256
            beta = (first_sign - (first_file * alpha)) % 256
            print("alpha: ", alpha)
            print("beta: ", beta)


        #print(inverses_alpha_mult)

        #print(alpha_mult, right_side)


    
