#!/usr/bin/python3

import asyncio
import json
import random
import uuid

async def sleeper() -> int:
    r = random.randint(0,5)
    await asyncio.sleep(r)
    return r

async def makePrint(s=bool) -> bool:
    assert type(s) == bool, 's is bool'
    u = uuid.uuid4()
    d = {'id':str(u)}
    j = json.dumps(d)
    r = await sleeper()
    assert type(r) == int, 'sleeper returns int'
    print(j)
    return True

async def main():
    t = []
    for i in range(0,5):
        t.append( makePrint(False) )
    r = await asyncio.gather(*t)
    for i in r:
        print(i)

asyncio.run(main(), debug=True)
