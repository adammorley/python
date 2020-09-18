#!/usr/bin/python3

import socket
import sys

addr = ('localhost', 7777)
conn = socket.create_connection(addr)
if not conn:
    print('error connecting')
    sys.exit(1)
conn.send('PING'.encode())
data = conn.recv(1024)
print("received", data.decode())
conn.close()
