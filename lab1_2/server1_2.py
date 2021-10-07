import threading
import socket

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'\n[ Server ] {nickname} left the chat!\n'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"[ Server ] Join with address {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"[ Server ] User login is  {nickname}!")
        broadcast(f"[ Server ] {nickname} join to the chat!\n".encode('ascii'))
        client.send(b'Connected to the server!')

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("\n[ Server ] Server starting successfully!\n")

receive()