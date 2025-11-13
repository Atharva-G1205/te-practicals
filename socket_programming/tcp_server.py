import socket
import threading

def handle_client(conn, addr):
    print(f"connected by {addr}")
    
    while True:
        data = conn.recv(1024).decode()
        
        if not data or data == 'exit':
            print(f"terminating connection with {addr}")
            break
        print(f"received from {addr}: {data}")
        conn.send(data.upper().encode())
    
    conn.close()

def tcp_server():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    tcp_server()
