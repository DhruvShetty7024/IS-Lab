from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Random.random import getrandbits, randint
from Crypto.Util.number import GCD
from phe import paillier

# ElGamal Functions
def generate_elgamal_keys(bits=1024):
    key = ElGamal.generate(bits, get_random_bytes)
    return key

def elgamal_encrypt(public_key, message):
    while True:
        k = randint(1, public_key.p - 2)
        if GCD(k, public_key.p - 1) == 1:
            break
    ciphertext = public_key.encrypt(message, k)
    return ciphertext

def elgamal_decrypt(private_key, ciphertext):
    return private_key.decrypt(ciphertext)

def elgamal_homomorphic_multiplication():
    # Generate keys
    key = generate_elgamal_keys()
    public_key = key.publickey()
    
    # Input two numbers to encrypt and multiply
    num1 = int(input("Enter the first number for ElGamal encryption: "))
    num2 = int(input("Enter the second number for ElGamal encryption: "))
    
    # Encrypt the numbers
    encrypted_num1 = elgamal_encrypt(public_key, num1)
    encrypted_num2 = elgamal_encrypt(public_key, num2)

    # Homomorphic multiplication
    multiplied_cipher = (encrypted_num1[0] * encrypted_num2[0], encrypted_num1[1] * encrypted_num2[1])
    
    # Decrypt to verify
    result = elgamal_decrypt(key, multiplied_cipher)
    print(f"Decrypted Result after Homomorphic Multiplication: {result}")
    print(f"Expected Result: {num1 * num2}")

# Paillier Functions
def paillier_data_sharing():
    # Generate Paillier key pair
    public_key, private_key = paillier.generate_paillier_keypair()

    # Input data from two parties
    data_party1 = int(input("Enter the data from Party 1: "))
    data_party2 = int(input("Enter the data from Party 2: "))
    
    # Encrypt data
    encrypted_data1 = public_key.encrypt(data_party1)
    encrypted_data2 = public_key.encrypt(data_party2)

    # Homomorphic addition
    combined_encrypted_data = encrypted_data1 + encrypted_data2

    # Decrypt to verify
    decrypted_result = private_key.decrypt(combined_encrypted_data)
    print(f"Decrypted Combined Result: {decrypted_result}")
    print(f"Expected Result: {data_party1 + data_party2}")

# Secure Thresholding (PHE for Multi-Party Computation)
def secure_thresholding():
    # Generate Paillier key pair
    public_key, private_key = paillier.generate_paillier_keypair()
    
    # Simulate inputs from three parties
    inputs = []
    for i in range(3):
        val = int(input(f"Enter the data from Party {i + 1}: "))
        inputs.append(public_key.encrypt(val))
    
    # Homomorphic addition to simulate aggregation
    aggregated_encrypted = inputs[0] + inputs[1] + inputs[2]

    # Decrypt the result to verify
    decrypted_result = private_key.decrypt(aggregated_encrypted)
    print(f"Decrypted Aggregated Result: {decrypted_result}")

# Main Menu Function
def menu():
    while True:
        print("\n=== PHE Operations Menu ===")
        print("1. ElGamal Homomorphic Multiplication")
        print("2. Paillier Secure Data Sharing")
        print("3. Secure Thresholding using Paillier")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            elgamal_homomorphic_multiplication()
        elif choice == '2':
            paillier_data_sharing()
        elif choice == '3':
            secure_thresholding()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    menu()
