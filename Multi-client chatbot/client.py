import socket
server_host = '127.0.0.1'
server_port = 1234

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((server_host,server_port))
while True:
    message = input("Enter your message: ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024)
    response = data.decode()
    print(f"Server response: {response}")