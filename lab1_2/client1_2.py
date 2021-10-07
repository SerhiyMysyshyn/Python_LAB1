import threading
from socket import *

nickname = input("[ Client ] Enter your login: ")

host = '127.0.0.1'
port = 55555
address = (host, port)

client = socket(AF_INET, SOCK_STREAM)
client.connect(address)

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("[ !!! ] Connection error!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()