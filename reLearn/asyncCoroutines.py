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

# do timeout stuff, also futures.  eg pass back a hashmap via a future and handle timeout via exception or somesuch
# also do task creation of multiple things and then go get the results after

asyncio.run(main(), debug=True)
asyncio.run(timeoutTest(), debug=True)
asyncio.run(poolExec(), debug=True)
