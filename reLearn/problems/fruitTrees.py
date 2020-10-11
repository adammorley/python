#!/usr/bin/python3

'''
There are n trees in a circle. Each tree has a fruit value associated with it. A bird can sit on a tree for 0.5 sec and then he has to move to a neighbouring tree. It takes the bird 0.5 seconds to move from one tree to another. The bird gets the fruit value when she sits on a tree. We are given n and m (the number of seconds the bird has), and the fruit values of the trees. We have to maximise the total fruit value that the bird can gather. The bird can start from any tree.
'''
'''
n = number of trees
dwell time = 0.5s (max?)

fv = [1,2,3,4...] < value of the fruit on a tree
m = # of seconds

so algo:

sort fv descending
assume instant harvest and no need to wait on a tree (so flight time is only metric)
if n < m/0.5, then need to know fruit regrowth time
else can just do:
m / 0.5 = number of trees to harvest
total harvest = sum(fv[0:(m/0.5)])
'''
