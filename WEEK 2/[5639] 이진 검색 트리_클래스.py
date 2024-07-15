import sys
sys.setrecursionlimit(10**8)
lines = sys.stdin.readlines()
pre = []
for line in lines:
    pre.append(int(line.strip()))

class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insertNode(self.root, val)

    def _insertNode(self, currentNode: Node, val):
        while True:
            if val < currentNode.val:
                if currentNode.leftChild == None:
                    currentNode.leftChild = Node(val=val)
                    break
                else:
                    currentNode = currentNode.leftChild
            else:
                if currentNode.rightChild == None:
                    currentNode.rightChild = Node(val=val)
                    break
                else:
                    currentNode = currentNode.rightChild

    def postorder_traversal(self, node: Node):
        if node.leftChild:
            self.postorder_traversal(node.leftChild)
        if node.rightChild:
            self.postorder_traversal(node.rightChild)
        print(node.val)

tree = BinarySearchTree()
for s in pre:
    tree.insert(s)

tree.postorder_traversal(tree.root)


