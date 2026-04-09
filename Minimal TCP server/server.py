import socket
server_ip = '127.0.0.1'
server_port = 1024

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((server_ip,server_port))
server_socket.listen(5)
print(f"Server is listening at the port {server_port}")
# client_socket, client_address = server_socket.accept()
# data = client_socket.recv(1024)
# print("Received Message:", data.decode())
# client_socket.send("Received your message.!".encode())


while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    try:
        while True:
            data = client_socket.recv(1024)

            # CRITICAL: Check if client closed the connection
            if not data:
                print("Client disconnected gracefully.")
                break

            print("Received Message:", data.decode())
            client_socket.send("Received your message.!".encode())
    except ConnectionAbortedError:
        print("Connection was lost abruptly.")
    finally:
        client_socket.close() # Clean up the resource
