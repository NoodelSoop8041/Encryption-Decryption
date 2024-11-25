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
                message += chr(((((char_code - (ord("a")-1)) * multiple) + shift) % 26) + (ord("a")-1))
            else:
                message += chr(((((char_code - (ord("A")-1)) * multiple)+ shift) % 26) + (ord("A")-1))
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
                    message += chr(((((char_code - (ord("a")-1)) - shift) * mod_inverse(multiple))%26) + (ord("a")-1))
                else:
                    message += chr(((((char_code - (ord("A")-1)) - shift) * mod_inverse(multiple))%26) + (ord("A")-1))
            else:
                message += char
        
    return message





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
        int(multiple)
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