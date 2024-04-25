# server.py
import socket
import threading

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Manual entry of keywords
    keywords = input("Enter keywords separated by commas (e.g., hi,bye): ").split(',')

    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Received data: {data}")
        detect_intrusion(data, keywords)

    client_socket.close()
    server_socket.close()
    print("Server stopped.")

def detect_intrusion(data, keywords):
    # Check if any keyword is present in the received data
    for keyword in keywords:
        if keyword.lower() in data.lower():
            print(f"Intrusion detected: '{keyword}' found in the data: '{data}'")

if __name__ == "__main__":
    start_server()
