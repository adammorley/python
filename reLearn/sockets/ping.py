#!/usr/bin/python3

import json
import socket
import sys

ping = json.dumps({'ping':True})
addr = ('localhost', 7777)
conn = socket.create_connection(addr)
conn.send(ping.encode())
data = conn.recv(1024)
print("received", data)
conn.close()
