from socket import *
import threading
import time

def connect():
    while True:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect(('localhost', 12345))

            name = input("Enter name: ")
            sock.send(name.encode())

            return sock

        except:
            print("Connection failed, retrying...")
            time.sleep(1)


client_socket = connect()

def send_message():
    while True:
        client_message = input()

        if client_message.lower() == "exit":
            client_socket.close()
            break
        else:
            client_socket.send(client_message.encode())


threading.Thread(target=send_message).start()

while True:
    try:
        message = client_socket.recv(1024).decode().strip()

        if message:
            print(message)

    except:
        print("Connection closed")
        break