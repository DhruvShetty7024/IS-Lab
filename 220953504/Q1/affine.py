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

def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char.upper()) - ord('A')
            encrypted_char = chr(((a * x + b) % 26) + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    a_inv = modinv(a, 26)
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            decrypted_char = chr(((a_inv * (y - b)) % 26) + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char
    
    return plaintext
    

a = 15
b = 20

ciphertext = affine_encrypt(plaintext, a, b)
print("Encrypted:", ciphertext)

decrypted_text = affine_decrypt(ciphertext, a, b)
print("Decrypted:", decrypted_text)
