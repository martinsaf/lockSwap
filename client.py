import socket
from cryptography.fernet import Fernet

# Load the key generated by the server
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

# File to be sent
file_to_send = 'file_to_send.txt'

# Encrypt the file
with open(file_to_send, 'rb') as file:
    file_data = file.read()

encrypted_data = cipher.encrypt(file_data)

# Client configuration
HOST = '127.0.0.1'  # Server's IP address
PORT = 65432        # Port number to connect to

# Create a socket and send the encrypted file
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(encrypted_data)
    print("Encrypted file sent to the server.")