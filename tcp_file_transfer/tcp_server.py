import socket

def tcp_server():
    host = "127.0.0.1"
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        command = conn.recv(4)
        if not command or command.decode(errors="ignore") == "EXIT":
            print("Connection closed by client.")
            break

        if command.decode(errors="ignore") == "HELL":
            _ = conn.recv(1)  # get the 'O' from 'HELLO'
            print("Hello message received from client.")
            conn.sendall("Hello from Server!".encode())

        elif command.decode(errors="ignore") == "FILE":
            filename_bytes = conn.recv(256)
            filename = filename_bytes.rstrip(b' ').decode(errors="ignore")
            filesize_bytes = conn.recv(32)
            filesize = int(filesize_bytes.rstrip(b' ').decode(errors="ignore"))
            print(f"Receiving file: {filename} ({filesize} bytes)")

            received = 0
            with open("received_" + filename, "wb") as f:
                while received < filesize:
                    chunk = conn.recv(min(4096, filesize - received))
                    if not chunk:
                        break
                    f.write(chunk)
                    received += len(chunk)
            print("File received successfully.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    tcp_server()
