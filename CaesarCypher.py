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


text = input("Enter your message: ")
while True:
    shift = input("Enter your value: ")
    try:
        int(shift)
    except ValueError:
        print("Please enter a number to shift by.")
        continue
    else:
        break
shift = int(shift)

e_d = input("Would you like to Encrypt or Decrypt a message?")

if e_d == "encrypt":
    print("Message:", caesar_cypher(text, shift))
elif e_d == "decrypt":
    print("Message:", caesar_cypher(text, -shift))