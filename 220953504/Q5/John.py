def decrypt_caesar_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        # Decrypt each character by shifting backward
        if char.isalpha():  # Check if the character is a letter
            # Calculate the original position
            shifted = ord(char) - shift
            if char.isupper():
                # Wrap around if necessary
                if shifted < ord('A'):
                    shifted += 26
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26
            plaintext += chr(shifted)
        else:
            plaintext += char  # Non-alphabetic characters are unchanged
    return plaintext

# Known plaintext and ciphertext pair
known_plaintext = "yes"
known_ciphertext = "CIW"

# Determine the shift by comparing the first characters
shift = (ord(known_ciphertext[0]) - ord(known_plaintext[0])) % 26

# Ciphertext found on the tablet
ciphertext_on_tablet = "XVIEWYWI"

# Decrypt the ciphertext using the determined shift
decrypted_text = decrypt_caesar_cipher(ciphertext_on_tablet, shift)
print("Decrypted Text:", decrypted_text)
