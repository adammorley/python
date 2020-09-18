#!/usr/bin/python3

import json
import logging
import socket

logger = logging.getLogger().setLevel(logging.INFO)

addr = ('localhost', 7777)
ss = socket.create_server(addr)
ss.listen()
while True:
    conn, addr = ss.accept()
    with conn:
        logging.info('connected {}'.format(addr))
        data = conn.recv(1024)
        logging.info('received {}'.format(data))
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
