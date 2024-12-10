#This is our key, simplified to include only lowercase letters
key = "mrandmrsdursleyofnumberfourprivetdrivewereproudtosaythattheywereperfectlynormalthankyouverymuch"
key_list = []
    
for char in key:
    key_list.append(ord(char) - 97)

text = input("Please enter your message:" )

def vigenere_encrypt(text):
    "Encrypts using the Vigenere Cipher"

    message = ""

    for i in range(len(text)):
        char = text[i]
        if char.islower():
            cipher_char = (ord(char) - 97)
            message += chr((cipher_char + key_list[i])%26 + 97)
        elif char.isupper():
            cipher_char = (ord(char) - 65)
            message += chr((cipher_char + key_list[i])%26 + 65)
        else:
            message += char

    return message


def vigenere_decrypt(text):
    "Decrypts using Vigenere Cypher"


    message = ""

    for i in range(len(text)):
        char = text[i]
        if char.islower():
            cipher_char = (ord(char) - 97)
            message += chr((cipher_char - key_list[i])%26 + 97)
        elif char.isupper():
            cipher_char = (ord(char) - 65)
            message += chr((cipher_char - key_list[i])%26 + 65)
        else:
            message += char

    return message

e_d = input("Would you like to Encrypt or Decrypt a message?")

if e_d.lower() == "encrypt":
    print("Message:", vigenere_encrypt(text))
elif e_d.lower() == "decrypt":
    print("Message:", vigenere_decrypt(text))