import socket
import threading


SERVER_IP = '127.0.0.1'
PORT = 55555
FORMAT = 'utf-8'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, PORT))
server_socket.listen()

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
            broadcast('{} left!'.format(nickname).encode(FORMAT))
            nicknames.remove(nickname)
            break
        

def receive():
    while True:
        client, address = server_socket.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode(FORMAT))
        client.send('Connected to server!'.encode(FORMAT))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()




print("Server is listening...")
receive()