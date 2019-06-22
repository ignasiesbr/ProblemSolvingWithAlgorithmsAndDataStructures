import timeit
import random

#Devise an experiment to verify that get item and set item are O(1) for dictionaries.

#t1 = timeit.Timer("dict.get(random.randint(0,len(dict)))", "from __main__ import random,dict")

# results = []
# for i in range(1, 10000000, 1000000):
#     dict = { "a" : 1}
#     for x in range(i):
#         dict[random.randint(0,i)] = random.randint(0,i)
#     pt = t1.timeit(number=1000)
#     results.append(pt)
#     dict = {}
# print(results)

# res from size 1 to 10m [0.0015503769999999362, 0.0016960010000000025, 0.0016811600000004034, 0.0016565799999987973,
# 0.0019659140000030106, 0.001634783000000084, 0.0028526389999967705, 0.0018008120000132521, 0.0030149579999942944,
# 0.0017256820000000062]

#ct time.

t2  =timeit.Timer("dict[random.randint(0,len(dict))] = random.randint(0,len(dict))" , "from __main__ import random, dict")
results2 = []
for i in range(1,1000000, 100000):
    dict = { "a" : 1}
    for x in range(i):
        dict[random.randint(0,i)] = random.randint(0,i)
    pt = t2.timeit(number = 1000)
    results2.append(pt)

print(results2)

#results from size 1 to 1m ->
#[0.0029004070000000493, 0.003068292000000028, 0.003016812999999896, 0.003152696999999982, 0.003008465999999821,
# 0.0033433059999996573, 0.0031786680000003287, 0.0030284079999987057, 0.0030886970000008063, 0.0032473060000004494]

#ct time
