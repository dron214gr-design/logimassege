from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

connection, address = server_socket.accept()

client_name = connection.recv(1024).decode()
connection.send(f"Вітаю {client_name} на сервері".encode())

command = connection.recv(1024).decode()

if command == 'NAME':
    connection.send(f"Твоє ім'я: {client_name}".encode())
elif command == 'EXIT':
    connection.send(f"Бувай, {client_name}".encode())
else:
    connection.send("Такої команди не існує".encode())

connection.close()
server_socket.close()