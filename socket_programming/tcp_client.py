import socket

def tcp_client():
    host = '127.0.0.1'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print("connected successfully")
    local_ip, local_port = client_socket.getsockname()

    print(local_ip, local_port)
    while True:
        message = input("enter message (type exit to quit): ")
        if message.lower() == 'exit':
            client_socket.send(message.encode())
            print("terminating connection")
            break
        
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()

        print(f"SERVER: {response}")

    client_socket.close()

if __name__ == '__main__':
    tcp_client()

