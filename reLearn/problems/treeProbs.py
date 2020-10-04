#!/usr/bin/python3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def height(self) -> int:
        if self is None:
            return 0
        rh = 0
        lh = 0
        if self.right is not None:
            rh = self.right.height()
        if self.left is not None:
            lh = self.left.height()
        if rh > lh + 1 or rh < lh - 1:
            return -1
        elif rh > lh:
            return 1 + rh
        elif lh > rh:
            return 1 + lh
        else:
            return 1

from collections import deque
class Tree:
    root: TreeNode
    def __init__(self, root=None):
        self.root = root
    def balanced(self) -> bool:
        if self.root.height() == -1:
            return False
        return True

r = TreeNode(val=5, left=TreeNode(val=3), right=TreeNode(val=6))
t = Tree(root=r)
assert t.balanced()
t.root.left.left = TreeNode(val=2)
assert t.balanced()
t.root.left.left.left = TreeNode(val=1)
assert not t.balanced()
t.root.left.right = TreeNode(val=2.5)
assert not t.balanced()
t.root.right.right = TreeNode(val=7)
assert t.balanced()


import itertools
from typing import Iterator
class TreeIterator:
    def __init__(self, root: TreeNode):
        def inorder_traverse(node) -> Iterator[int]:
            if not node:
                return
            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        self.inorder = inorder_traverse(root)
        def levelorder_traverse(node) -> Iterator[int]:
            if not node:
                return
            yield node.val
            yield from levelorder_traverse(node.left)
            yield from levelorder_traverse(node.right)
        self.levelorder = levelorder_traverse(root)
    def baseNext(self, generator) -> int:
        assert generator is not None
        try:
            return next(generator)
        except StopIteration:
            return
    def baseHasNext(self, generator) -> bool:
        assert generator is not None
        u, c = itertools.tee(generator)
        generator = u
        try:
            next(c)
        except StopIteration:
            return False
        return True
class InorderTreeIterator(TreeIterator):
    def next(self) -> int:
        return self.baseNext(self.inorder)
    def hasNext(self) -> bool:
        return self.baseHasNext(self.inorder)
class LevelorderTreeIterator(TreeIterator):
    def next(self) -> int:
        return self.baseNext(self.levelorder)
    def hasNext(self) -> bool:
        return self.baseHasNext(self.levelorder)

iti = InorderTreeIterator(t.root)
print(iti.next())
print(iti.next())

lti = LevelorderTreeIterator(t.root)
print(lti.next())
print(lti.next())
