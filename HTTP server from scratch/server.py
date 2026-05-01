import socket

def start_server():
    # 1. Create a socket object
    # AF_INET = IPv4, SOCK_STREAM = TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Allow the port to be reused immediately after closing
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 3. Bind to host and port
    host = '127.0.0.1'
    port = 8080
    server_socket.bind((host, port))

    # 4. Start listening for incoming connections (max 1 queued connection)
    server_socket.listen(1)
    print(f"Serving at http://{host}:{port} ...")

    while True:
        # 5. Accept a new connection
        client_connection, client_address = server_socket.accept()

        # 6. Receive the request data (usually the first 1024 bytes is enough for basic headers)
        request = client_connection.recv(1024).decode()
        print(f"Request received:\n{request}")

        # 7. Prepare a simple HTTP response
        # Note: The blank line (\r\n\r\n) between headers and body is MANDATORY.
        response_body = "<html><body><h1>Hello from your scratch-built server!</h1></body></html>"

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n"
            f"Content-Length: {len(response_body)}\r\n"
            "Connection: close\r\n"
            "\r\n"
            f"{response_body}"
        )

        # 8. Send the response and close the connection
        client_connection.sendall(response.encode())
        client_connection.close()

if __name__ == "__main__":
    start_server()
