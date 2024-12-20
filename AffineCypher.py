def mod_inverse(multiple):
    """Finds the inverse of the encryption multiple under mod 26"""

    for x in range(1, 26):
        if (multiple*x) % 26 == 1:
            return x
    return None


def affine_encrypt(text, multiple, shift):
    """Encrypts a text using the Affine Cypher"""

    message = ""

    for char in text:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                cipher_char = ((char_code - (96)) * multiple)
                message += chr((cipher_char+shift)%26 + 96)
            else:
                cipher_char = ((char_code - (64)) * multiple)
                message += chr((cipher_char+shift)%26 + 64)
        else:
            message += char
    
    return message

def affine_decrypt(text, multiple, shift):
    """Decrypts a text using the Affine Cypher"""

    message = ""

    for char in text:
            if char.isalpha():
                char_code = ord(char)
                if char.islower():
                    cipher_char = (mod_inverse(multiple)*(char_code - (96 + shift)))
                    message += chr(cipher_char%26 + 96)
                else:
                    cipher_char = (mod_inverse(multiple)*(char_code - (64 + shift)))
                    message += chr(cipher_char%26 + 64)
            else:
                message += char
        
    return message



mult = [1,3,5,7,9,11,15,17,19,21,23,25]

text = input("Enter your message: ")

while True:
    multiple = input("Enter your multiple: ")
    try:
        int(multiple)
    except ValueError:
        print("Please enter a number multiple")
        continue
    else:
        break

while True:
    shift = input("Enter your shift: ")
    try:
        int(shift)
    except ValueError:
        print("Please enter a number shift")
        continue
    else:
        break

multiple = int(multiple)
shift = int(shift)

e_d = input("Would you like to encrypt or decrypt a message?: ")
if e_d == "encrypt":
     print("Message:", affine_encrypt(text, multiple, shift))
elif e_d == "decrypt":
    print("Message:", affine_decrypt(text, multiple, shift))