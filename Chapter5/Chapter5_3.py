import timeit
import random


def binarySearchRecursive(item, loi, first, last):
    mid = (first + last) // 2
    if first > last:
        return False
    if loi[mid] == item:
        return True
    else:
        if loi[mid] > item:
            return binarySearchRecursive(item, loi, first, mid - 1)
        else:
            return binarySearchRecursive(item, loi, mid + 1, last)


# Benchmark.

t1 = timeit.Timer("binarySearchRecursive(random.randint(0,len(l) - 1), l, 0, len(l) - 1)", "from __main__ import random, l, binarySearchRecursive")


l = []
res = []
for i in range(1, 100000,10000):
    for x in range(i):
        l.append(random.randint(1, i))
    r1 = t1.timeit(number=1000)
    res.append(r1)
    l = []

print(res)


# Res:

# [0.0037773899999999916, 0.011942951000000201, 0.012735994000000028, 0.013020283999999993, 0.014467239999999881,
# 0.013914427999999868, 0.01421912400000025, 0.015166602000000307, 0.015015877999999816, 0.015227818999999698]

# with slice operator:

#[0.003992114000000102, 0.056091799999999914, 0.10759368899999999, 0.1695034580000001, 0.22652603999999998,
# 0.2822885639999999, 0.365565975, 0.6298199979999994, 0.5301599860000001, 0.6239519429999998]