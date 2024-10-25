from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from hashlib import sha256

# Confidentiality: RSA Encryption and Decryption
def generate_rsa_keys():
    # Generate RSA key pair (private and public keys)
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(public_key, message):
    # Encrypt a message using the recipient's public key
    rsa_public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def rsa_decrypt(private_key, encrypted_message):
    # Decrypt the encrypted message using the private key
    rsa_private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

# Integrity: SHA-256 Hashing
def hash_message(message):
    # Generate SHA-256 hash of the message
    return sha256(message.encode()).hexdigest()

# Authenticity: Digital Signature (RSA-based)
def sign_message(private_key, message):
    # Sign the message by creating a digital signature using the sender's private key
    rsa_private_key = RSA.import_key(private_key)
    hash_obj = SHA256.new(message.encode())
    signature = pkcs1_15.new(rsa_private_key).sign(hash_obj)
    return signature

def verify_signature(public_key, message, signature):
    # Verify the digital signature using the sender's public key
    rsa_public_key = RSA.import_key(public_key)
    hash_obj = SHA256.new(message.encode())
    try:
        pkcs1_15.new(rsa_public_key).verify(hash_obj, signature)
        return True
    except (ValueError, TypeError):
        return False

def demonstrate_cia_triad():
    # Original message to demonstrate the CIA triad
    message = "Confidential and Secure Communication"
    
    # Step 1: Confidentiality
    print("\n--- Confidentiality ---")
    sender_private_key, sender_public_key = generate_rsa_keys()  # Sender's key pair
    recipient_private_key, recipient_public_key = generate_rsa_keys()  # Recipient's key pair
    
    encrypted_message = rsa_encrypt(recipient_public_key, message)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypting the message to show confidentiality
    decrypted_message = rsa_decrypt(recipient_private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
    
    # Step 2: Integrity
    print("\n--- Integrity ---")
    original_hash = hash_message(message)
    print(f"Original Hash: {original_hash}")

    # Simulate verification by the recipient
    received_hash = hash_message(decrypted_message)
    if original_hash == received_hash:
        print("Integrity Verified: Hashes match.")
    else:
        print("Integrity Verification Failed: Hashes do not match.")
    
    # Step 3: Authenticity (and Integrity)
    print("\n--- Authenticity ---")
    # Sender signs the original message to ensure authenticity and integrity
    signature = sign_message(sender_private_key, message)
    print(f"Digital Signature: {signature}")

    # Recipient verifies the signature using the sender's public key
    if verify_signature(sender_public_key, message, signature):
        print("Authenticity Verified: Signature is valid.")
    else:
        print("Authenticity Verification Failed: Signature is invalid.")

if __name__ == "__main__":
    demonstrate_cia_triad()
