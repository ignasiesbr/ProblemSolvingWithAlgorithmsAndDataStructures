# Design an experiment to compare the performance of the py list with the linked list.
import timeit
import random
from Chapter3_13to19 import UnorderedList

t1 = timeit.Timer("l1.append(random.random())", "from __main__ import random, l1")
t2 = timeit.Timer("l2.append(random.random())", "from __main__ import random, l2")

l1 = []
l2 = UnorderedList()
res1 = []
res2 = []
for i in range(1000, 100000, 10000):
    pt1 = t1.timeit(number=1000)
    pt2 = t2.timeit(number=1000)
    res1.append(pt1)
    res2.append(pt2)

#res1 =  [0.00028382599999998703, 0.0001261449999998554, 0.00012568100000009963, 0.00012521700000012181,
# 0.0001210440000001256, 0.0001247529999996999, 0.0001303189999997123, 0.00013124600000047337, 0.0001284639999994397,
# 0.0001228979999998714]

#res2 =[0.06751851400000008, 0.2005455759999999, 0.341864336, 0.48889856600000003, 0.6699139669999998, 0.753277561,
# 0.871266034, 1.0232602579999996, 1.1521120199999997, 1.2844981549999996]

#The performance is way lower in our implementation. Append with python lists is O(1) and in our implementation is
# O(n)
