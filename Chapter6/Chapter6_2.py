# Modify buildParseTree and evaluate to handle boolean statements.
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

def buildParseTree(expr):
    lot = expr.split()
    tree = BinaryTree("")
    posStack = Stack()
    posStack.push(tree)
    currentTree = tree

    for token in lot:
        if token == "(":
            currentTree.insertLeft("")
            posStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif token == ")":
            currentTree = posStack.pop()
        elif token in ["and", "or"]:
            currentTree.setRootVal(token)
            currentTree.insertRight("")
            posStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif token == "not":
            parent = posStack.pop()
            currentTree = parent
            currentTree.setRootVal(token)
            posStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif token in ["1", "0"]:
            currentTree.setRootVal(int(token))
            parent = posStack.pop()
            currentTree = parent
    return tree

def evaluate(tree):
    opers = {"and":operator.and_, "or":operator.or_, "not":operator.not_}
    leftC = tree.getLeftChild()
    rightC = tree.getRightChild()
    if leftC and not rightC:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(leftC))
    if leftC and rightC:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return tree.getRootVal()

expr = " ( ( 1 and 0 ) or ( 1 and ( not 0 ) ) ) "
print(evaluate(buildParseTree(expr)))
# EXP : 1
