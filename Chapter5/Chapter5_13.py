# 13. Perform a benchmark on shell sort.
import random
import timeit

from ShellSort import gapInsertionSort, shellSort

# generate random integer list.

l = [random.randint(1,500) for i in range(1000)]
l2 = l.copy()
l3 = l.copy()


t1 = timeit.Timer("shellSort(l)", "from __main__ import shellSort, l")
t2 = timeit.Timer("shellSort2(l2)", "from __main__ import shellSort2, l2")
t3 = timeit.Timer("shellSort3(l3)", "from __main__ import shellSort3, l3")

def shellSort2(l):
    sublistcount = len(l) // 2
    for i in range(sublistcount):
        gapInsertionSort(l,i,2)
    gapInsertionSort(l,0,1)

def shellSort3(l):
    sublistcount = len(l) // 3
    for i in range(sublistcount):
        gapInsertionSort(l,i,3)
    gapInsertionSort(l,0,1)

r1 = t1.timeit(number=1)
r2 = t2.timeit(number=1)
r3 = t3.timeit(number=1)

print(str(r1) + " " + str(r2) + " " + str(r3))

# Results:
# 0.006709794000000047          0.12053374100000003     0.06887046000000008
# using n/2 -> n/4 and so on    using gap = 2           using gap = 3