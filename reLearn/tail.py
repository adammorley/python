#!/usr/bin/python3

fileName = 'README'
n = 5
lines = []
try:
    with open(fileName, 'r') as inFile:
        for line in inFile:
            lines.append(line)
            if len(lines) > n:
                lines.pop(0)
except Exception as e:
    print('got an error reading: {}'.format(e))

for line in lines:
    print(line.rstrip())
