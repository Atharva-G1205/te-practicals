import socket

def udp_server():
    host = "127.0.0.1"
    port = 65433

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")

        if data.decode()=='exit':
            print('server disconnecting')
            break

        server_socket.sendto(data.upper(), addr)  # Echo back
    server_socket.close()


if __name__ == "__main__":
    udp_server()
