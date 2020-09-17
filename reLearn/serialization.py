#!/usr/bin/python3

import json

jsonString = '{"nuts":123,"foo":456,"bar":true}'
print(type(jsonString))
print(json.loads(jsonString))
blob = {
        'nuts': 444,
        'cars': 654,
        'bugs': 'hips',
        'set': True
       }

print(type(blob))
print(json.dumps(blob))

