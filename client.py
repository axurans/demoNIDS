# client.py
import socket

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter a message (type 'rshift+enter' to stop): ")
        client_socket.send(message.encode('utf-8'))

        # Check for the termination command
        if message.lower() == 'rshift+enter':
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
