#!/usr/bin/python3

with open('testIn', 'r') as inFile:
    for line in inFile:
        print(line)

with open('testOut', 'w') as outFile:
    outFile.write('hi bobo\n')
    outFile.write('bye bobo')

with open('testOut', 'r') as outFile:
    for line in outFile:
        print(line)
