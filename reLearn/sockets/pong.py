#!/usr/bin/python3

import socket

addr = ('localhost', 7777)
ss = socket.create_server(addr)
ss.listen()
conn, addr = ss.accept()
with conn:
    print('connected', addr)
    data = conn.recv(1024)
    print('received:', data)
    # total buffer overflow in my head b/c c!
    if data.decode().rstrip() == 'PING':
        conn.send('PONG'.encode())
    else:
        conn.send('FAIL'.encode())
