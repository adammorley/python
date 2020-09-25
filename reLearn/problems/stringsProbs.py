#!/usr/bin/python3

s = 'saveChangesInTheEditor'
n = 1
for i in range(0, len(s)):
    if s[i].isupper():
        n += 1
print(n)


strs=['eat','tea','tan','ate','nat','bat']
new = []
for i in strs:
    new.append( ''.join(sorted(i)) )
print(new)
track = {}
for i in range(0,len(strs)):
    try:
        track[new[i]]
    except KeyError:
        track[new[i]] = []
    track[ new[i] ].append(strs[i])
out = []
for k, v in track.items():
    out.append(v)
print(out)

def substring(s, t) -> bool:
    index = 0
    for i in s:
        state = False
        for j in range(index, len(t)):
            if i == t[j]:
                index = j + 1
                state = True
                break
        if state == False: # didn't find character
            return  False
    return True

s = 'abc'
t = 'ahbgdc'
print(substring(s, t))

s = 'anagram'
t = 'nagaram'
ss = sorted(s)
tt = sorted(t)
assert ss == tt

s = 'rat'
t = 'car'
ss = sorted(s)
tt = sorted(t)
assert ss != tt


