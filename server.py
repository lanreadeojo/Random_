# echo-server.py

import socket
import datetime

HOST = "127.0.0.1" # Standard loopback interface address(localhost)
PORT = 65432 # ports to listen on(non-privileged ports are nums > 1023)

# Create a server socket using the with statement
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # bind() takes in a tuple of the host's address and the port used to listen
    s.bind((HOST,PORT))
    # listen() receives a queue of connections. The max length is unspecified so the system assign a max
    # length of the queue
    s.listen()
    # accept() pauses and waits for an incoming connection. When a client socket connects it returns
    # a new socket object representing the connection (conn) and tuple of the address (addr) which
    # contains the Host and a port
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

