def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start - shift) % 26)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text
text = input("Enter Text: ")
key = 20
encrypted_message = encrypt(text, key)
print(f"Encrypted Message: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")

