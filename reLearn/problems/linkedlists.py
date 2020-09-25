#!/usr/bin/python3

class LinkedNode:
    nextNode = None
    value = None
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        pieces = []
        for k, v in self.__dict__.items():
            pieces.append('{}:{}'.format(k, v))
            return ','.join(pieces)
    def getValue(self):
        assert self.value != None
        return self.value
    def getNext(self):
        assert self.nextNode != None
        return self.nextNode
    def setNext(self, nextNode):
        assert type(nextNode) == LinkedNode
        self.nextNode = nextNode
    def setValue(self, value):
        assert value != None
        self.value = value

class LinkedList:
    head: LinkedNode
    def __init__(self, head):
        assert type(head) == LinkedNode
        self.head = head
    def __repr__(self):
        pieces = []
        for k, v in self.__dict__.items():
            pieces.append('{}:{}'.format(k, v))
            return ','.join(pieces)
    def getHead(self):
        assert type(head) == LinkedNode
        return self.head

head = LinkedNode(5)
node = LinkedNode(6)
head.setNext(node)
Llist = LinkedList(head)
print(head)
print(node)
print(Llist)

# or just use a deque
from collections import deque
Llist = deque()
Llist.append(5)
Llist.append(6)
print(Llist)

left = deque([2,4,3])
right = deque([5,6,4])

def getNum(vals):
    num = 0
    for i in range(len(vals)-1, -1, -1):
        num += vals[i] * 10**i
    return num

L = getNum(left)
R = getNum(right)
NN = L+R

def makeNum(num):
    r = deque()
    while num != 0:
        p = num % 10
        r.append(p)
        num = int(num / 10)
    return r

nv = makeNum(NN)
print(nv)

left = deque([1,3,6,9])
right = deque([2,3,6,9,10])
def merge(one, two):
    new = deque()
    oneP = 0
    twoP = 0
    while oneP < len(one) and twoP < len(two):
        if oneP == len(one) and twoP < len(two):
            new.append(two[twoP])
            twoP += 1
        elif oneP < len(one) and twoP == len(two):
            new.append(one[oneP])
            oneP += 1
        elif one[oneP] <= two[twoP]:
            new.append(one[oneP])
            oneP += 1
        elif two[twoP] < one[oneP]:
            new.append(two[twoP])
            twoP += 1
        else:
            assert True, 'blah'
    return new

new = merge(left, right)
print(new)

node0 = LinkedNode(1)
node1 = LinkedNode(17)
node0.setNext(node1)
node2 = LinkedNode(6)
node1.setNext(node2)
LL = LinkedList(node0)
prev = LL.getHead()
nn = prev.getNext()
while nn.getNext() != None:
    nn = prev.getNext()
    nodeM = LinkedNode(nn.getValue)
    nodeM.setNext(prev)
    tmp = nn.getNext()
    prev = nn
    nn = tmp


