# lockSwap

## Description
A Python-based system for securely transferring files between a client and server using encryption. Files are encrypted on the client, sent over a TCP connection, and decrypted on the server.

## Prerequisites
- Python installed on both machines.
- Install dependencies:
  ```bash
  pip install cryptography

## Usage
- Run the server:
  ```bash
  python server.py
- Prepera a file (file_to_send.txt) in the client directory.
- Run the client to send the file:
  ```bash
  python client.py
