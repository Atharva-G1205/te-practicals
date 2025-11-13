import socket
import os

def say_hello(client_socket):
    client_socket.sendall("HELLO".encode())
    server_msg = client_socket.recv(1024).decode()
    print(f"Server says: {server_msg}")

def send_file(client_socket):
    filename = input("Enter filename to send: ")
    if not os.path.exists(filename):
        print("File does not exist!")
        return

    client_socket.sendall(b"FILE")
    basename = os.path.basename(filename)
    client_socket.sendall(basename.encode().ljust(256, b' '))  # fixed 256 bytes for filename
    filesize = os.path.getsize(filename)
    client_socket.sendall(str(filesize).encode().ljust(32, b' '))  # fixed 32 bytes for filesize

    with open(filename, "rb") as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            client_socket.sendall(data)
    print("File sent successfully.")

def tcp_client():
    host = "127.0.0.1"
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Connected to server.")

    while True:
        print("\nClient Menu:")
        print("1. Say Hello")
        print("2. Send File")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            say_hello(client_socket)
        elif choice == "2":
            send_file(client_socket)
        elif choice == "3":
            client_socket.sendall("EXIT".encode())
            break
        else:
            print("Invalid choice!")

    client_socket.close()

if __name__ == "__main__":
    tcp_client()

