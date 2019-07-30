from pythonds.basic import Stack
from pythonds.basic import Queue
from pythonds.trees import BinaryTree
import operator

# Extend the function to handle expressions without whitespaces

def buildParseTree(expr):
    lot = convertToList(expr)
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in lot:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

def convertToList(expr):
    q = Queue()
    l = []
    enteringNumber = False
    for char in expr:
        if char in ['+', '-', '*', '/', ')', '(']:
            if enteringNumber:
                enteringNumber = False
                s = ""
                while not q.isEmpty():
                    s = s + str(q.dequeue())
                l.append(s)
            l.append(char)
        elif char != " ":
            q.enqueue(char)
            enteringNumber = True
    return l




# Expression with withespaces and without them. Worst case
expr = " ( 3+(10* 20)) "
print(evaluate(buildParseTree(expr)))
