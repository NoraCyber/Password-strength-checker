message = input("Enter message: ")
shift = 3

encrypted = ""

for char in message:
    if char.isalpha():
        ascii_offset = 65 if char.isupper() else 97
        encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        encrypted += encrypted_char
    else:
        encrypted += char

print("Encrypted Message:", encrypted)