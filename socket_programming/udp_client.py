import socket

def udp_client():
    host = "127.0.0.1"
    port = 65433

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message (type 'exit' to quit): ")
        if message.lower() == "exit":
            client_socket.sendto(message.encode(), (host, port))
            break
        client_socket.sendto(message.encode(), (host, port))
        data, _ = client_socket.recvfrom(1024)
        print(f"Server: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    udp_client()

