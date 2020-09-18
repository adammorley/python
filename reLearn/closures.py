#!/usr/bin/python3

def xmit(msg):
    def xmitter():
        print(msg)
    xmitter()

print(xmit('hi'))

def print_msg(num):
    def printer():
        nonlocal num
        num = 3
        print(num)
    printer()
    print(num)

print_msg(5)
