#!/usr/bin/python3

def is_palindrome(string: str) -> bool:
    # treat string as array and use two counters to compare, skipping spaces
    # termination condition is pointers meeting or crossing
    string = string.replace(' ','')
    odd = True
    mid = int(len(string) / 2)
    if len(string) % 2 == 0:
        odd = False
    i = 0
    j = len(string) - 1
    if odd:
        while (i < mid) and (j > mid):
            if string[i] != string[j]:
                return False
            i, j = i+1, j-1
    elif not odd:
        while (i < mid) and (j >= mid):
            if string[i] != string[j]:
                return False
            i, j = i+1, j-1
    else:
        raise Exception
    return True

string = 'race car'
assert is_palindrome(string)
string = 'race cat'
assert not is_palindrome(string)
string = 'racee car'
assert is_palindrome(string)
