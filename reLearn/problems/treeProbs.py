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
from collections import deque
class TreeIterator:
    def __init__(self, root: TreeNode):
        def inorder_traverse(node) -> Iterator[int]:
            if not node:
                return
            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        self.inorder = inorder_traverse(root)
        def preorder_traverse(node) -> Iterator[int]:
            if not node:
                return
            yield node.val
            yield from preorder_traverse(node.left)
            yield from preorder_traverse(node.right)
        self.preorder = preorder_traverse(root)
        def postorder_traverse(node) -> Iterator[int]:
            if not node:
                return
            yield from postorder_traverse(node.left)
            yield from postorder_traverse(node.right)
            yield node.val
        self.postorder = postorder_traverse(root)
        def levelorder_traverse() -> Iterator[int]:
            self.q = deque()
            self.q.append(root)
            while len(self.q) != 0:
                node = self.q.popleft()
                yield node.val
                if node.left is not None:
                    self.q.append(node.left)
                if node.right is not None:
                    self.q.append(node.right)
        self.levelorder = levelorder_traverse()
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
class PreorderTreeIterator(TreeIterator):
    def next(self) -> int:
        return self.baseNext(self.preorder)
    def hasNext(self) -> bool:
        return self.baseHasNext(self.preorder)
class PostorderTreeIterator(TreeIterator):
    def next(self) -> int:
        return self.baseNext(self.postorder)
    def hasNext(self) -> bool:
        return self.baseHasNext(self.postorder)
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
print(lti.next())

#iterate through the tree and stick all the vals into a hash w/ count then return the highest valued keys from the hash (using a sort)

# iterate through a "tree" stored as an array (implied parent/child) and use a counter to find the most common element, then find any which are similarly most common.  uses extra memory tho.
from collections import Counter
l = [1,3,2,7,5,5,3,6]
c = Counter(v for v in l)
m = c.most_common(1)[0][1]
r = [k for k, v in c.items() if v == m]
print(r, c, m)

r2 = TreeNode(val=5, left=TreeNode(val=3), right=TreeNode(val=6))
t2 = Tree(root=r2)
t2.root.left.left = TreeNode(val=3)
t2.root.left.left.left = TreeNode(val=1)
t2.root.left.right = TreeNode(val=4)
t2.root.right.right = TreeNode(val=7)
t2.root.right.left = TreeNode(val=6)

def invertTree(node: TreeNode): # in-place
    if node is None:
        return
    node.left, node.right = node.right, node.left
    invertTree(node.left)
    invertTree(node.right)
    return

print(t2.root.val, t2.root.left.val, t2.root.right.val, t2.root.left.left.val, t2.root.right.right.val)
invertTree(t2.root)
print(t2.root.val, t2.root.left.val, t2.root.right.val, t2.root.left.left.val, t2.root.right.right.val)

r2 = TreeNode(val=4, left=TreeNode(val=2), right=TreeNode(val=6))
t2 = Tree(root=r2)
t2.root.left.left = TreeNode(val=1)
t2.root.left.right = TreeNode(val=3)
t2.root.right.left = TreeNode(val=5)
t2.root.right.right = TreeNode(val=7)

def findKthElement(root: TreeNode, k: int) -> int:
    if k < 1:
        return None
    c = 1
    it = InorderTreeIterator(root)
    while i := it.next():
        if k == c:
            return i
        c += 1
    return None
    
assert findKthElement(r2, 2) == 2
assert findKthElement(r2, 5) == 5
assert findKthElement(r2, 8) == None


def minDepth(root: TreeNode) -> int:
    def leaf_node(node: TreeNode) -> bool:
        assert node is not None
        return (node.left is None) and (node.right is None)
    # level order traverse with termination condition == leaf node
    # level order is just a queue
    q = deque([(root, 1), ])
    while q:
        node, depth = q.popleft()
        if node:
            if leaf_node(node):
                return depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))

def SameTree(root1: TreeNode, root2: TreeNode) -> bool:
    def is_same_node(a, b):
        if (not a) and (not b):
            return True
        if a and b:
            return (a.val == b.val) and is_same_node(a.left, b.left) and is_same_node(a.right, b.right)
        return False
    return is_same_node(root1, root2)

def findTree(node: TreeNode, val: int) -> TreeNode:
    if node is None:
        return None
    elif node.val == val:
        return node
    elif val < node.val:
        return findTree(node.left)
    elif val > node.val:
        return findTree(node.right)
    else:
        raise Exception

def serialize_tree(root: TreeNode) -> list:
    q = deque(root)
    t = []
    while q:
        n = q.popleft()
        if n is None:
            t.append(None) # <-- need to store a sentinel like # or % or whatever if string
        else:
            t.append(n.val)
        q.append(n.left)
        q.append(n.right)
    return t

def deserialize_tree(tree: list) -> TreeNode:
    root = TreeNode(val=tree.popleft())
    q = deque([root,])
    while q:
        n = q.popleft()
        lv = tree.popleft()
        if lv is not None:
            n.left = TreeNode(val=lv)
            q.append(n.left)
        rv = tree.popleft() # need to test for IndexError in case at end of tree
        if rv is not None:
            n.right = TreeNode(val=rv)
            q.append(n.right)
    return root

def univalued_tree(root: TreeNode) -> bool:
    def inorder(node: TreeNode) -> Iterator[int]:
        if node is None:
            return
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)
    g = inorder(root)
    v = root.val
    for i in g:
        if v != i:
            return False
    return True

r2 = TreeNode(val=4, left=TreeNode(val=2), right=TreeNode(val=6))
r2.left.left = TreeNode(val=1)
r2.left.right = TreeNode(val=3)
r2.right.left = TreeNode(val=5)
r2.right.right = TreeNode(val=7)

assert not univalued_tree(r2)
r3 = TreeNode(val=1, left=TreeNode(val=1), right=TreeNode(val=1))
r3.left = TreeNode(val=1)
r3.right = TreeNode(val=1)
assert univalued_tree(r3)

def assert_bst(node: TreeNode) -> bool:
    if node is None:
        return True
    if (node.left is not None) and node.left.val >= node.val:
        return False
    if (node.right is not None) and node.right.val <= node.val:
        return False
    l = assert_bst(node.left)
    r = assert_bst(node.right)
    return l and r

assert assert_bst(r2)
assert not assert_bst(r3)
