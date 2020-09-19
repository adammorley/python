#!/usr/bin/python3

import asyncio
import concurrent.futures
import logging
import time

logging.basicConfig(level=logging.DEBUG)

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print('started at {}'.format(time.strftime('%X')))
    #task1 = asyncio.create_task(say_after(2, 'world'))
    #print('task type: {}'.format(type(task1)))
    #task2 = asyncio.create_task(say_after(1, 'hello'))
    #await task1
    #await task2
    await asyncio.gather(say_after(2, 'world'), say_after(1, 'hello'))
    print('finished at {}'.format(time.strftime('%X')))


async def timeoutTest():
    print('starting timeout test')
    try:
        await asyncio.wait_for(asyncio.sleep(5), 3)
    except asyncio.TimeoutError as e:
        print('got a timeout on > <')
    try:
        await asyncio.wait_for(asyncio.sleep(3), 5)
    except asyncio.TimeoutError as e:
        print('got a timeout on < >')
    print('finished waiting')

def blocking_io():
    'file io can block!'
    with open('/dev/urandom', 'rb') as ur:
        return ur.read(100)

def cpu_bound():
    'somebody said use process pool for cpu bound'
    return sum(i*i for i in range(10**7))

async def poolExec():
    loop = asyncio.get_running_loop()

    with concurrent.futures.ThreadPoolExecutor() as p:
        r = await loop.run_in_executor(p, blocking_io)
        print('custom pool blocking io {}'.format(r))

    print('before')
    with concurrent.futures.ProcessPoolExecutor() as p:
        r = await loop.run_in_executor(p, cpu_bound)
        print('custom pool cpu bound {}'.format(r))
    print('after')

import json

async def pinger():
    r, w = await asyncio.open_connection('localhost', 7777)
    w.write(json.dumps({'ping':True}).encode())
    await w.drain()
    d = await r.read(100)
    j = json.loads( d.decode() )
    print('received: {}'.format(j))
    w.close()
    await w.wait_closed()
    return j

async def execer():
    t = []
    for i in range(30):
        t.append(pinger())
    r = await asyncio.gather(*t)
    print('type: {} of object: {}'.format(type(r), r))
    if isinstance(r, type([])):
        print('type of first elem: {}'.format(type(r[0])))

# many at once execution
asyncio.run(execer(), debug=True)

# basic task exec
#asyncio.run(main(), debug=True)

# timeouts
asyncio.run(timeoutTest(), debug=True)

# different executors for blocking calls
#asyncio.run(poolExec(), debug=True)
