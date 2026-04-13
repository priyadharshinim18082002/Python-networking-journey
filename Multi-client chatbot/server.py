import socket
import threading
def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        message = message.decode()
        print(f"Messsage received from {client_socket} :",message)
        client_socket.send("Hello Client".encode())
    client_socket.close()


def main():
    server_host = '127.0.0.1'
    server_port = 1234
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((server_host,server_port))
    server_socket.listen(5)
    print(f"Server listening on {server_host}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    main()
