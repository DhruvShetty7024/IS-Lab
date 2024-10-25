import socket
from hashlib import sha256

def start_server(host='127.0.0.1', port=65432):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address and port
        server_socket.bind((host, port))
        # Enable the server to accept connections (1 connection at a time)
        server_socket.listen()
        print(f"Server started at {host}:{port}. Waiting for a connection...")
        
        # Wait for a client to connect
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            reassembled_message = ""
            
            # Receive data in chunks until "END" is received
            while True:
                data = conn.recv(1024).decode('utf-8')
                if data == "END":
                    break
                reassembled_message += data
            
            print(f"Reassembled message: {reassembled_message}")

            # Compute the hash of the reassembled message using SHA-256
            message_hash = sha256(reassembled_message.encode()).hexdigest()
            print(f"Computed Hash: {message_hash}")

            # Send the hash back to the client for verification
            conn.sendall(message_hash.encode())

if __name__ == "__main__":
    start_server()
