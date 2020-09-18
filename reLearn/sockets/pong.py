#!/usr/bin/python3

import json
import socket

addr = ('localhost', 7777)
ss = socket.create_server(addr)
ss.listen()
while True:
    conn, addr = ss.accept()
    with conn:
        print('connected', addr)
        data = conn.recv(1024)
        print('received:', data)
        try:
            b = data.decode()
            msg = json.loads(b)
            if msg['ping']:
                conn.send(
                    json.dumps(
                        {'pong':True}
                    ).encode()
                )
        except:
            conn.send(
                json.dumps(
                    {'fail':True}
                ).encode()
            )
