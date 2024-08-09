import numpy as np

# Function to preprocess the plaintext (remove spaces, make uppercase, and pad if necessary)
def preprocess_text(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'  # Pad with 'X' if length is odd
    return text

# Function to convert characters to numerical values (A=0, B=1, ..., Z=25)
def char_to_num(char):
    return ord(char) - ord('A')

# Function to convert numerical values back to characters
def num_to_char(num):
    return chr(num + ord('A'))

# Function to encipher a pair of characters using the Hill cipher
def encipher_pair(pair, key_matrix):
    pair_vector = np.array([[char_to_num(pair[0])], [char_to_num(pair[1])]])
    cipher_vector = np.dot(key_matrix, pair_vector) % 26
    return num_to_char(cipher_vector[0, 0]) + num_to_char(cipher_vector[1, 0])

# Function to encipher the entire message
def hill_encipher(plaintext, key_matrix):
    processed_text = preprocess_text(plaintext)
    ciphertext = ""
    
    for i in range(0, len(processed_text), 2):
        pair = processed_text[i:i+2]
        ciphertext += encipher_pair(pair, key_matrix)
    
    return ciphertext

# Define the key matrix
key_matrix = np.array([[3, 3], [2, 7]])

# The message to be enciphered
plaintext = "We live in an insecure world"

# Encipher the message
ciphertext = hill_encipher(plaintext, key_matrix)
print("Ciphertext:", ciphertext)
