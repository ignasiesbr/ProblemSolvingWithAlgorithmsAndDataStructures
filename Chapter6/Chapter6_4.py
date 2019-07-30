# Modify the code for a binary search tree to make it threaded. Write a non-recursive inorder traversal method for the
# threaded binary search tree. A threaded binary tree maintains a reference from each node to its successor.

# Look at the _put methods and the constructor of TreeNode to see the implementation of threaded Binary Tree.


class TreeNode:
    def __init__(self, data, key = None, right = None, left = None, parent = None, rightThread = False):
        self.payload = data
        self.key = key
        self.rightChild = right
        self.leftChild = left
        self.parent = parent
        self.rightThreaded = rightThread

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def isRightThreaded(self):
        return self.rightThreaded

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getData(self):
        return self.payload


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val, currentNode.leftChild)
            else:
                if currentNode.rightThreaded == True:
                    currentNode.rightThreaded = False
                    temp = currentNode.rightChild
                    currentNode.rightChild = TreeNode(val, key, right=temp, parent=currentNode, rightThread=True)
                else:
                    currentNode.leftChild = TreeNode(val, key, right=currentNode, parent=currentNode, rightThread=True)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                if currentNode.rightThreaded == True:
                    currentNode.rightThreaded = False
                    temp = currentNode.rightChild
                    currentNode.rightChild = TreeNode(val, key, right=temp, parent=currentNode, rightThread=True)
                else:
                    currentNode.rightChild = TreeNode(val, key)

    def __setitem__(self,k,v):
       self.put(k,v)

    def getMostLeft(self, currentNode):
        while currentNode.hasLeftChild():
            currentNode = currentNode.leftChild
        return currentNode

    def traverse(self):
        current = self.getMostLeft(self.root)
        while current.rightChild != None:
            print(current.payload)
            current = current.rightChild
        print(current.payload)



t = BinaryTree()

t[4] = 4
t[5] = 5
t[3] = 3
t[1] = 1
t[2] = 2
t[6] = 6
t[7] = 7
