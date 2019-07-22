# 12. Implement Selection sort using simultaneous assignment.
import random


def selectionSort(alist):
    for i in range(len(alist) - 1, 0 , -1):
        posmax = 0
        for x in range(1, i + 1):
            if alist[x] > alist[posmax]:
                posmax = x
        alist[posmax], alist[i] = alist[i], alist[posmax]

l = [random.randint(1,100) for i in range(20)]
selectionSort(l)



