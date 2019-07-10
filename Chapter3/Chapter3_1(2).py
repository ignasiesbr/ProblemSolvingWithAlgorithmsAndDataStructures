from pythonds.basic.stack import Stack

def infixEval(infixExpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    operandStack = Stack()
    operatorStack = Stack()
    tokenList = infixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(token)
            if (not operatorStack.isEmpty()):
                op2 = operandStack.pop()
                op1 = operandStack.pop()
                operator = operatorStack.pop()
                res = doMath(op1, op2, operator)
                operandStack.push(res)
        else:
            operatorStack.push(token)

    return(operandStack.pop())

def doMath(a, b, op):
    if op == "*":
        return int(a) * int(b)
    elif op == "/":
        return int(a) / int(b)
    elif op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)

