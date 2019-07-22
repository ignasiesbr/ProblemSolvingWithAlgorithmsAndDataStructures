# Set up an experiment to test the difference between seq search and a binary search.
import timeit
import random


def seqSearch(item, loi):
    found = False
    pos = len(loi) - 1
    while not found and pos >=0:
        if item == loi[pos]:
            found = True
        pos = pos - 1
    return found


def binarySearch(item, loi):
    first = 0
    last = len(loi) - 1
    found = False

    while not found and first <= last:
        mid = (first + last) // 2
        if loi[mid] == item:
            found = True
        else:
            if item<loi[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


t1 = timeit.Timer("seqSearch(random.randint(0, len(l) - 1), l)", "from __main__ import random, l, seqSearch")
t2 = timeit.Timer("binarySearch(random.randint(0,len(l) - 1), l)", "from __main__ import random, l, binarySearch")

l = []
resSeq = []
resBin = []
for i in range(1, 100000, 10000):
    for x in range(i):
        l.append(random.randint(1, i))
    l.sort()
    r1 = t1.timeit(number=1000)
    r2 = t2.timeit(number=1000)
    l = []
    resSeq.append(r1)
    resBin.append(r2)

print(resSeq)
print(resBin)

#Results:
# Seq:
# [0.003284403999999963, 1.4158973140000002, 2.738698324, 4.1821786990000005, 5.755287766, 7.684073421999997,
# 9.486967889999999, 10.868819539999997, 12.164729431000005, 13.984605224999996]

#   Binary:
# [0.003645214999999924, 0.008910372999999971, 0.009642198999999962, 0.010006257000000573, 0.010791414999999915,
#  0.011293676000001085, 0.0112885750000018, 0.011904458000003615, 0.011946197000000325, 0.012171123999991096]

# Massive difference
