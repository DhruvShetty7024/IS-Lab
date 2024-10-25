import rsa
import hashlib
import time

# Function to perform RSA encryption
def rsa_encrypt(public_key, message):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

# Function to perform RSA decryption
def rsa_decrypt(private_key, encrypted_message):
    decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
    return decrypted_message

# Function to generate a digital signature using RSA
def create_signature(private_key, message):
    message_hash = hashlib.sha256(message.encode()).hexdigest()  # Hash the message
    signature = rsa.sign(message.encode(), private_key, 'SHA-256')
    return signature, message_hash

# Function to verify the digital signature
def verify_signature(public_key, signature, message):
    try:
        rsa.verify(message.encode(), signature, public_key)
        return True
    except rsa.VerificationError:
        return False

# Function to display current time
def current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

# Main menu-driven program
def menu():
    # Generate RSA keys
    (public_key, private_key) = rsa.newkeys(512)

    while True:
        print("\n=== RSA Encryption and Digital Signature Menu ===")
        print("1. RSA Encryption")
        print("2. RSA Decryption")
        print("3. Create Digital Signature")
        print("4. Verify Digital Signature")
        print("5. Exit")
        
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted_message = rsa_encrypt(public_key, message)
            print(f"[{current_time()}] Encrypted Message: {encrypted_message.hex()}")

        elif choice == '2':
            encrypted_message_hex = input("Enter the encrypted message in hex format: ")
            encrypted_message = bytes.fromhex(encrypted_message_hex)
            decrypted_message = rsa_decrypt(private_key, encrypted_message)
            print(f"[{current_time()}] Decrypted Message: {decrypted_message}")

        elif choice == '3':
            message = input("Enter the message to sign: ")
            signature, message_hash = create_signature(private_key, message)
            print(f"[{current_time()}] Signature: {signature.hex()}")
            print(f"[{current_time()}] Message Hash: {message_hash}")

        elif choice == '4':
            message = input("Enter the original message: ")
            signature_hex = input("Enter the signature in hex format: ")
            signature = bytes.fromhex(signature_hex)
            is_valid = verify_signature(public_key, signature, message)
            if is_valid:
                print(f"[{current_time()}] Signature is valid.")
            else:
                print(f"[{current_time()}] Signature is invalid.")

        elif choice == '5':
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    menu()
