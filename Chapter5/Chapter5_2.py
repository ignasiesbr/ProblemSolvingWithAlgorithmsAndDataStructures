# Binary recursive vs binary iterative.
import timeit
import random

def binSearchIterative(item, loi):
    found = False
    first = 0
    last = len(loi) - 1

    while not found and first <= last:
        mid = (first + last) // 2
        if loi[mid] is item:
            found = True
        else:
            if loi[mid] > item:
                last = mid - 1
            else:
                first = mid + 1
    return found

def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearch(alist[:mid], item)
            else:
                return binarySearch(alist[mid + 1:], item)


l = [1,2,3,5,7,10,15,24,32,46,78]

print(binarySearch(l, 3))

# Experiment.

t1 = timeit.Timer("binSearchIterative(random.randint(0,len(l) - 1), l)", "from __main__ import random, l, binSearchIterative")
t2 = timeit.Timer("binarySearch(l, random.randint(0,len(l) - 1))", "from __main__ import random, l, binarySearch")

#generate random l.
l = []
resIt = []
resRec = []
for i in range(1,100000, 10000):
    for x in range(i):
        l.append(random.randint(1,i))
    l.sort()
    r1 = t1.timeit(number=1000)
    r2 = t2.timeit(number=1000)
    resIt.append(r1)
    resRec.append(r2)
    l = []

print(resIt)
print(resRec)

# Results:
#Iterative
# [0.003623882999999939, 0.009246140999999986, 0.009832343000000021, 0.010109676999999984, 0.011129501999999736,
# 0.011761154000000218, 0.01594155800000019, 0.012248110000000256, 0.012532864000000643, 0.012658544999999854]

# Recursive
#[0.003992114000000102, 0.056091799999999914, 0.10759368899999999, 0.1695034580000001, 0.22652603999999998,
# 0.2822885639999999, 0.365565975, 0.6298199979999994, 0.5301599860000001, 0.6239519429999998]


#The recursive results are worse because the slice operator that takes O(n) to compute.
