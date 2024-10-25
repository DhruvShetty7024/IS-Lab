import socket
from hashlib import sha256

def send_message_in_parts(host='127.0.0.1', port=65432, message="Hello, this is a test message!"):
    # Break the original message into parts (10 characters each)
    message_parts = [message[i:i+10] for i in range(0, len(message), 10)]

    # Compute the SHA-256 hash of the original message for later verification
    original_hash = sha256(message.encode()).hexdigest()
    print(f"Original Message Hash: {original_hash}")

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((host, port))

        # Send each part of the message separately
        for part in message_parts:
            client_socket.sendall(part.encode())
        
        # Send "END" to notify the server that the message is fully sent
        client_socket.sendall("END".encode())

        # Receive the hash from the server
        received_hash = client_socket.recv(1024).decode('utf-8')
        print(f"Received Hash from Server: {received_hash}")

        # Verify the integrity of the message by comparing hashes
        if original_hash == received_hash:
            print("Integrity check passed: The message is intact.")
        else:
            print("Integrity check failed: The message has been altered.")

if __name__ == "__main__":
    # Test the function with a sample message
    send_message_in_parts(message="This is a sample message that will be sent in parts.")
