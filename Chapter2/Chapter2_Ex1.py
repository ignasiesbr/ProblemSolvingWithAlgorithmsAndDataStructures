import timeit
import random
#1. Devise an experiment to verify that the list index operator is O(1)

t1 = timeit.Timer("ls[random.randint(0,len(ls))]", "from __main__ import random, ls")
results = []
for i in range(1000, 10000000, 100000):
    ls = list(range(0,i))
    pt = t1.timeit(number=1000)
    results.append(pt)
    ls = []

print(results)

#2.


