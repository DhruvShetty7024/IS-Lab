plaintext = input("Enter Text: ")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def multiplicative_cipher_encrypt(plaintext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26.")
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            num = ord(char.upper()) - ord('A')
            encrypted_num = (num * key) % 26
            encrypted_char = chr(encrypted_num + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

def multiplicative_cipher_decrypt(ciphertext, key):
    mod_inverse = modinv(key, 26)
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            num = ord(char.upper()) - ord('A')
            decrypted_num = (num * mod_inverse) % 26
            decrypted_char = chr(decrypted_num + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    
    return plaintext

key = 3

ciphertext = multiplicative_cipher_encrypt(plaintext, key)
print("Encrypted:", ciphertext)

decrypted_text = multiplicative_cipher_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
