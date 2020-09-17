#!/usr/bin/python3

outFileName = 'testOut'
inFileName = 'testIn'

with open(inFileName, 'r') as inFile:
    for line in inFile:
        print('read a line from the file: {}'.format(line))

string = 'this is text to put in out file'
with open(outFileName, 'w') as outFile:
    outFile.write(string)

with open(outFileName, 'r') as inFile:
    for line in inFile:
        print('lines written to file: {}'.format(line))
