import socket

def udp_server():
    host = "127.0.0.1"
    port = 65433

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDP server listening on {host}:{port}...")

    while True:
        data, client_addr = server_socket.recvfrom(1024)
        if data == b"EXIT":
            print("server shutting down.")
            break
        if data.startswith(b"FILENAME:"):
            filename = data[len(b"FILENAME:"):].decode(errors="ignore")
        else:
            print("invalid protocol. expected FILENAME.")
            continue

        print(f"receiving file: {filename}")
        with open("received_" + filename, "wb") as f:
            while True:
                chunk, _ = server_socket.recvfrom(1024)
                if chunk == b"EOF":
                    break
                f.write(chunk)
        print(f"file {filename} received successfully.")

    server_socket.close()

if __name__ == "__main__":
    udp_server()