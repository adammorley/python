#!/usr/bin/python3

import json
import logging
import socket
import sys

logger = logging.getLogger().setLevel(logging.INFO)

ping = json.dumps({'ping':True})
addr = ('localhost', 7777)
conn = socket.create_connection(addr)
conn.send(ping.encode())
data = conn.recv(1024)
logging.info('received {}'.format(data))
conn.close()
