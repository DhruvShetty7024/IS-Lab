def vigenere_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()

            plaintext_index = alphabet.index(char)
            key_index_value = alphabet.index(key[key_index % len(key)])

            encrypted_index = (plaintext_index + key_index_value) % 26
            encrypted_char = alphabet[encrypted_index]

            if not is_upper:
                encrypted_char = encrypted_char.lower()
            
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char
    
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    plaintext = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()

            ciphertext_index = alphabet.index(char)
            key_index_value = alphabet.index(key[key_index % len(key)])

            decrypted_index = (ciphertext_index - key_index_value) % 26
            decrypted_char = alphabet[decrypted_index]

            if not is_upper:
                decrypted_char = decrypted_char.lower()
            
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    
    return plaintext
plaintext = input("Enter Text: ")
key = "dollars"

ciphertext = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)

