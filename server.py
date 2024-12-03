import socket
from cryptography.fernet import Fernet

# Generate a key and save it on the server
key = Fernet.generate_key()
cipher = Fernet(key)

with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Server configuration
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 65432      # Port number to listen on

# Set up the server to receive data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Server listening on port", PORT)

    conn, addr = server.accept()
    with conn:
        print('Connected by', addr)
        # Receive the encrypted file
        with open('received_encrypted_file', 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        print("Encrypted file received.")

# Decrypt the received file
with open('received_encrypted_file', 'rb') as enc_file:
    encrypted_data = enc_file.read()

decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted file
with open('received_file', 'wb') as dec_file:
    dec_file.write(decrypted_data)

print("File decrypted and saved as 'received_file'.")
