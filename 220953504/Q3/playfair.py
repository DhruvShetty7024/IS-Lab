import string

# Function to create the Playfair cipher key square
def create_key_square(keyword):
    # Remove duplicates from the keyword and keep the order
    keyword = "".join(sorted(set(keyword), key=keyword.index))
    
    # Prepare the rest of the alphabet (excluding 'J' which is usually combined with 'I')
    alphabet = "".join([c for c in string.ascii_uppercase if c != 'J'])
    
    # Concatenate the keyword with the remaining letters of the alphabet
    key_square = keyword + "".join([c for c in alphabet if c not in keyword])
    
    # Create a 5x5 matrix for the key square
    return [key_square[i:i+5] for i in range(0, 25, 5)]

# Function to preprocess the plaintext
def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    processed_text = ""
    i = 0
    while i < len(text):
        processed_text += text[i]
        # If a pair of identical letters is found, insert 'X' between them
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += 'X'
        i += 1
    # If the length of the text is odd, append an 'X' to the end
    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    return processed_text

# Function to find the position of a letter in the key square
def find_position(letter, key_square):
    for row in range(5):
        for col in range(5):
            if key_square[row][col] == letter:
                return row, col
    return None

# Function to encipher a pair of letters
def encipher_pair(pair, key_square):
    row1, col1 = find_position(pair[0], key_square)
    row2, col2 = find_position(pair[1], key_square)
    
    # Rule 1: Same row, shift right
    if row1 == row2:
        return key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
    
    # Rule 2: Same column, shift down
    elif col1 == col2:
        return key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
    
    # Rule 3: Rectangle, swap columns
    else:
        return key_square[row1][col2] + key_square[row2][col1]

# Function to encipher the entire message
def playfair_encipher(plaintext, keyword):
    key_square = create_key_square(keyword)
    processed_text = preprocess_text(plaintext)
    ciphertext = ""
    
    for i in range(0, len(processed_text), 2):
        pair = processed_text[i:i+2]
        ciphertext += encipher_pair(pair, key_square)
    
    return ciphertext

# The secret key and the message to be enciphered
keyword = "GUIDANCE"
plaintext = "The key is hidden under the door pad"

# Encipher the message
ciphertext = playfair_encipher(plaintext, keyword)
print("Ciphertext:", ciphertext)

