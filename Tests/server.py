import socket

FORMAT = 'utf-8'
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'


# server = socket.create_server('127.0.0.1', 10000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 10000))
server.listen(4)
print("Start working ...")
client_socket, address = server.accept()
data = client_socket.recv(1024).decode(FORMAT)
print(data)
data_2 = "Тестирование в рамках семинара 6".encode(FORMAT)
client_socket.send(HDRS.encode(FORMAT) + data_2)
print("Shutdown...")