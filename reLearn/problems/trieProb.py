#!/usr/bin/python3

import string
class pointers:
    letters: dict
    def __init__(self):
        self.letters = dict()
        for l in string.ascii_lowercase:
            self.letters[l] = None

class node:
    state: bool = False
    letter: str
    p = dict
    def __init__(self):
        self.p = dict() 
        for l in string.ascii_lowercase:
            self.p[l] = None
    def set_letter(self, letter):
        assert len(letter) == 1
        self.letter = letter
    def store(self):
        self.state = True

class rootNode(node):
    def __init__(self):
        super().__init__()
        # no letter 

class trie:
    root: rootNode
    def __init__(self):
        self.root = rootNode()
        self.state = None
    def insert(self, word):
        cur = self.root
        for i in range(0, len(word)):
            l = word[i]
            if cur.p[l] is None:
                cur.p[l] = node()
            cur = cur.p[l]
            if i == len(word) - 1:
                cur.state = True
    def search(self, word):
        cur = self.root
        for i in range(0, len(word)):
            l = word[i]
            if cur.p[l] is None:
                return False
            cur = cur.p[l]
            if i == len(word) - 1:
                return cur.state
    def startsWith(self, word):
        cur = self.root
        for i in range(0, len(word)):
            l = word[i]
            if cur.p[l] is None:
                return False
            cur = cur.p[l]
            if i == len(word) - 1:
                return True

t = trie()
t.insert('apple')
assert t.search('apple')
assert not t.search('app')
assert t.startsWith('app')
t.insert('app')
assert t.search('app')
