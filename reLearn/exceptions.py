#!/usr/bin/python3

a = 1
try:
    b = a[0]
    print(b)
except (IndexError, TypeError) as err:
    print('got error, problem with a: {}'.format(err))
