def additive_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            
            shifted_index = (alphabet.index(char) + key) % 26
            encrypted_char = alphabet[shifted_index]
            
            if not is_upper:
                encrypted_char = encrypted_char.lower()
            
            ciphertext += encrypted_char
        else:
            ciphertext += char 
    
    return ciphertext


def additive_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            
            # Reverse shift the character
            shifted_index = (alphabet.index(char) - key) % 26
            decrypted_char = alphabet[shifted_index]
            
            if not is_upper:
                decrypted_char = decrypted_char.lower()
            
            plaintext += decrypted_char
        else:
            plaintext += char
    
    return plaintext


try:
    key = int(input("Enter the key (integer): "))
plaintext = input("Enter the text to encrypt: ")

ciphertext = additive_encrypt(plaintext, key)
decrypted_text = additive_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)

