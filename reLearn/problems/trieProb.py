#!/usr/bin/python3

from strings import ascii_lowercase as alpha
class pointers:
    letters: dict
    def __init__(self):
        self.letters = dict()
        for l in alpha:
            self.letters[l] = None

class node:
    state: bool = None
    letter: str
    p = None
    def __init__(self):
        self.p = pointers()
    def set_letter(self, letter):
        assert len(letter) == 1
        self.letter = letter
    def store(self):
        self.state = True

class root(node):
    def __init__(self):
       super().__init__()

class trie:
    root
    def __init__(self):
        self.root = root()
    def insert(self, word):
        
    def search(self, word):
    def startsWith(self, word):
