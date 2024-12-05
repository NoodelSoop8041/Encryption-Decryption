def vigenere_encrypt(text):
    "Encrypts using the Vigenere Cipher"

    #This is our key, simplified to include only lowercase letters
    key = "mrandmrsdursleyofnumberfourprivetdrivewereproudtosaythattheywereperfectlynormalthankyouverymuch"
    list = []
    
    for char in key:
        list.append(ord(char) - 96)

    message = ""
    for char in text:
        if not char.isalpha():
            message += char
        if char.islower():
            cipher_char = (ord(char) - 96)
            message += chr(cipher_char + list[key])
        else:
            cipher_char = (ord(char) - 64)

    return message



text = input("Please enter your message:" )

print(vigenere_encrypt(text))