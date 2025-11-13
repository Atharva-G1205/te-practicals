import socket
import os

def send_file(client_socket, host, port):
    filename = input("enter filename to send: ")
    if not os.path.exists(filename):
        print("file does not exist!")
        return

    client_socket.sendto(b"FILENAME:" + os.path.basename(filename).encode(), (host, port))

    with open(filename, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.sendto(data, (host, port))

    client_socket.sendto(b"EOF", (host, port))
    print(f"file {filename} sent successfully.")

def udp_client():
    host = "127.0.0.1"
    port = 65433

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        print("\n====== UDP file transfer client ======")
        print("1. send file")
        print("2. exit")
        choice = input("enter your choice: ")

        if choice == "1":
            send_file(client_socket, host, port)
        elif choice == "2":
            client_socket.sendto(b"EXIT", (host, port))
            print("exiting client.")
            break
        else:
            print("invalid choice!")
    client_socket.close()

if __name__ == "__main__":
    udp_client()

