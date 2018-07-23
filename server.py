# import socket
# import cgi
# import re
#
# serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
# serv_sock.bind(('127.0.0.1', 53210))
# serv_sock.listen(10)
# while True:
#     client_sock, client_addr = serv_sock.accept()
#     print('Connected by', client_addr)
#     while True:
#         data = client_sock.recv(1024)
#         decoded_data = str(data.decode('utf-8'))
#         print(decoded_data)
#         if decoded_data.startswith('GET /index.html HTTP/1.1'):
#             decoded_data = decoded_data.replace('GET', 'POST')
#             server_data = bytes(decoded_data, 'utf-8')
#             client_sock.sendall(server_data)
#             print(decoded_data)
#             break
#         # ([A-Za-z0-9]+\s\/I?index.html)
#         if not data:
#             break
#         client_sock.sendall(data)
#     client_sock.close()
#     print('Disconnected by', client_addr)
from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):

    def do_GET(self): #Overriding BaseHTTPRequestHandler
        if self.path == '/':
            self.path = '/index.html'
        try:
            file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()
