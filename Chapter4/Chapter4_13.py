import math

def f(row,col):
    return int(math.factorial(row) / (math.factorial(col) * (math.factorial(row - col))))


def pascalTriangle(nrows):
    s = " "
    for i in range(nrows):
        for x in range(i + 1):
            s = s + " " + str(f(i,x))
        s = s + " \n "
    return s

