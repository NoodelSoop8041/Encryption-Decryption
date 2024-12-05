def caesar_cypher(text, shift):
    """Encrypts and Decrypts a text using the Caesar Cypher"""
    
    message = ""

    for char in text:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                message += chr(((char_code - ord("a") + shift) % 26) + ord("a"))
            else:
                message += chr(((char_code - ord("A") + shift) % 26) + ord("A"))
        else:
            message += char
    
    return message



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


text = input("Enter your message: ")


cypher = input("Would you like to use Caesar or Affine? ")
e_d = input("Would you like to Encrypt or Decrypt a Message? ")

#If affine is selected, adds multiple var for input
if cypher.lower() == "affine":
    while True:
        multiple = input("Enter your multiple: ")
        try:
            int(multiple)
        except ValueError:
            print("Please enter a number multiple")
            continue
        else:
            break
    multiple = int(multiple)

while True:
    shift = input("Enter your shift: ")
    try:
        int(shift)
    except ValueError:
        print("Please enter a number shift")
        continue
    else:
        break

shift = int(shift)

#Checks for caesar or affine, then executes according to encrypt or decrypt or each
if cypher.lower() == "caesar":
    if e_d.lower() == "encrypt":
        print("Message:", caesar_cypher(text, shift))
    else:
        print("Message:", caesar_cypher(text, -shift))
elif cypher.lower() == "affine":
    if e_d.lower() == "encrypt":
        print("Message:", affine_encrypt(text, multiple, shift))
    else:
        print("Message:", affine_decrypt(text, multiple, shift))

