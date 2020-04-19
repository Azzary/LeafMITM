import socket


while True:
    socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.connect(("127.0.0.1",5555))