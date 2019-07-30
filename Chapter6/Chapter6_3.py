# 3. Using the findSuccesor method, write a non-recursive inorder traversal for a binary search tree.
from pythonds.basic import Stack
from pythonds.trees import BinaryTree

# Inorder traversal using a Stack

def inorderTrav(tree):
    posStack = Stack()
    current = tree

    while current != None or posStack.size()>0:
        # Left-most node
        while (current != None):
            posStack.push(current)
            current = current.getLeftChild()
        current = posStack.pop()
        print(current.getRootVal())

        current = current.getRightChild()



tree = BinaryTree("A")
tree.insertLeft("B")
tree.getLeftChild().insertLeft("C")
tree.getLeftChild().insertRight("D")
tree.insertRight("E")
inorderTrav(tree)

