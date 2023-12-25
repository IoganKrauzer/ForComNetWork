import socket

FORMAT = 'utf-8'
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 10000))
        server.listen(4)
        while True:
            print("Start working ...")
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode(FORMAT)

            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Shutdown...")
    
    
def load_page_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    parc = request_data.split(' ')[1]
    response = ''
    try:
        with open('view'+parc, 'rb') as file:
            response = file.read()
        return HDRS.encode(FORMAT) + response
    except FileNotFoundError:
        return (HDRS_404 + "No page found").encode(FORMAT)
        


if __name__ == '__main__':
    start_server()
    