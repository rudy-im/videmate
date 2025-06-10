import socket

HOST = '127.0.0.1'
PORT = 9999

with socket.create_connection((HOST, PORT)) as sock:
    sock.sendall("shutdown".encode("utf-8"))
