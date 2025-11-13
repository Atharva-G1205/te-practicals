import socket 
import os

def tcp_server():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("listening")

    conn, addr = server_socket.accept()

    while True:
        command = conn.recv(4)

        if command == "EXIT":
            print("terminating")
            break
        elif command == "HELL":
            _ = conn.recv(1)
            conn.sendall("hello from server".encode())
        elif command == "FILE":
            filename = conn.recv(256).rstrip(b" ").decode(errors="ignore")
            filesize = int(conn.recv(32).rstrip(b" ").decode(errors="ignore"))

            received = 0

            with open(f"received_{filename}", 'wb') as f:
                while received < filesize:
                    data = conn.recv(min(4096, filesize - received))
                    if not data:
                        break

                    f.write(data)
                    received += len(data)

    conn.close()
    server_socket.close()

