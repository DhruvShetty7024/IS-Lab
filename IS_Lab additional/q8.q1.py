import subprocess

def encrypt_data(file_path, recipient):
    """
    Encrypt a file using the recipient's public key. 
    This ensures confidentiality for secure storage and transmission.
    """
    output_file = "encrypted_data.gpg"
    try:
        subprocess.run(["gpg", "--output", output_file, "--encrypt", "--recipient", recipient, file_path], check=True)
        print(f"File '{file_path}' encrypted successfully as '{output_file}'.")
    except subprocess.CalledProcessError:
        print("Error during encryption.")

def decrypt_data(encrypted_file):
    """
    Decrypt an encrypted file using the private key.
    This allows secure retrieval of the original data.
    """
    output_file = "decrypted_data.txt"
    try:
        subprocess.run(["gpg", "--output", output_file, "--decrypt", encrypted_file], check=True)
        print(f"File '{encrypted_file}' decrypted successfully as '{output_file}'.")
    except subprocess.CalledProcessError:
        print("Error during decryption.")

def sign_data(file_path):
    """
    Create a digital signature for a file using the sender's private key.
    This ensures authenticity and integrity of the file.
    """
    signature_file = "data.sig"
    try:
        subprocess.run(["gpg", "--output", signature_file, "--sign", file_path], check=True)
        print(f"File '{file_path}' signed successfully. Signature saved as '{signature_file}'.")
    except subprocess.CalledProcessError:
        print("Error during signing.")

def verify_signature(signature_file, data_file):
    """
    Verify the digital signature against the original data file.
    This confirms that the file was not tampered with and was signed by the sender.
    """
    try:
        subprocess.run(["gpg", "--verify", signature_file, data_file], check=True)
        print("Signature verified successfully.")
    except subprocess.CalledProcessError:
        print("Signature verification failed.")

def menu():
    while True:
        print("\n=== GnuPG Operations Menu ===")
        print("1. Encrypt Data (Secure Storage/Transmission)")
        print("2. Decrypt Data")
        print("3. Sign Data (Digital Signature Creation)")
        print("4. Verify Signature")
        print("5. Exit")
        
        choice = input("Choose an option (1/2/3/4/5): ")
        
        if choice == '1':
            file_path = input("Enter the path of the file to encrypt: ")
            recipient = input("Enter the recipient name/email: ")
            encrypt_data(file_path, recipient)
        elif choice == '2':
            encrypted_file = input("Enter the path of the encrypted file: ")
            decrypt_data(encrypted_file)
        elif choice == '3':
            file_path = input("Enter the path of the file to sign: ")
            sign_data(file_path)
        elif choice == '4':
            signature_file = input("Enter the path of the signature file: ")
            data_file = input("Enter the path of the original data file: ")
            verify_signature(signature_file, data_file)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    menu()
