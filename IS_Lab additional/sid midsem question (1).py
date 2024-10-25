from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import time

# Auditor logs
audit_log = []

def log_audit(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    audit_log.append(f"[{timestamp}] {event}")
    print(f"Auditor Log: {event}")

# Customer: Encrypts Data and Signs it
def customer_menu():
    print("\n--- Customer Menu ---")
    patient_data = input("Enter message to encrypt: ")
    
    # Generate RSA keys
    customer_key = RSA.generate(2048)
    customer_private_key = customer_key.export_key()
    customer_public_key = customer_key.publickey().export_key()

    # Encrypt patient data using public key
    cipher_rsa = PKCS1_OAEP.new(customer_key.publickey())
    encrypted_data = cipher_rsa.encrypt(patient_data.encode())
    
    # Hash the encrypted data using SHA-256
    hash_obj = SHA256.new(encrypted_data)
    
    # Sign the hash of the encrypted data
    signature = pkcs1_15.new(customer_key).sign(hash_obj)
    
    print("Data encrypted and signed.")
    log_audit("Customer encrypted and signed data.")
    
    return encrypted_data, signature, customer_public_key, customer_private_key

# Merchant: Verifies Signature and Processes Transaction
def merchant_menu(encrypted_data, signature, customer_public_key):
    print("\n--- Merchant Menu ---")
    
    # Import customer's public key
    customer_key = RSA.import_key(customer_public_key)
    
    # Hash the encrypted data to verify the signature
    hash_obj = SHA256.new(encrypted_data)
    
    try:
        # Verify the signature
        pkcs1_15.new(customer_key).verify(hash_obj, signature)
        print("Signature is valid.")
        log_audit("Merchant verified a valid signature.")
        
        # Process the transaction
        print("Merchant processed the transaction.")
        log_audit("Merchant processed a transaction.")
    except (ValueError, TypeError):
        print("Signature is invalid!")
        log_audit("Merchant found an invalid signature.")

# Auditor: Reviews Logs and Displays Actions
def auditor_menu():
    print("\n--- Auditor Menu ---")
    print("Audit Log History:")
    for log_entry in audit_log:
        print(log_entry)

# Main Menu Function
def main_menu():
    encrypted_data = None
    signature = None
    customer_public_key = None
    
    while True:
        print("\n--- Security System Main Menu ---")
        print("1. Customer Actions")
        print("2. Merchant Actions")
        print("3. Auditor Actions")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            encrypted_data, signature, customer_public_key, _ = customer_menu()
        elif choice == '2':
            if encrypted_data and signature and customer_public_key:
                merchant_menu(encrypted_data, signature, customer_public_key)
            else:
                print("No customer data available. Please complete a customer transaction first.")
        elif choice == '3':
            auditor_menu()
        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main_menu()
