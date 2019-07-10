#6. Design and implement an experiment to benchmark the two Queue ADT
import timeit
import random

from pythonds.basic.queue import Queue
from Chapter3_5 import Queue2

q1 = Queue()
q2 = Queue2()

#It is going to be checked the enqueue / dequeue in both queues.
t1 = timeit.Timer("q1.enqueue(random.random())" , "from __main__ import random, q1")
t2 = timeit.Timer("q2.enqueue(random.random())", "from __main__ import random, q2")
resEnqueue1 = []
resEnqueue2 = []
for i in range(1, 100000, 10000):
    for x in range(i):
        q1.enqueue(random.random())
        q2.enqueue(random.random())
    pt = t1.timeit(number=1000)
    pt2 = t2.timeit(number=1000)
    resEnqueue1.append(pt)
    resEnqueue2.append(pt2)

print("Results of enqueue operation, first the given ADT, second our ADT")
print(resEnqueue1)
print(resEnqueue2)

#Dequeue. We expect that our implementation is slower due the pop(0).

t3 = timeit.Timer("q1.dequeue()", "from __main__ import q1")
t4 = timeit.Timer("q2.dequeue()", "from __main__ import q2")

resDequeue1 = t3.timeit(number=1000)
resDequeue2 = t4.timeit(number=1000)

print("Results of dequeue operation, first the given ADT, second our ADT")
print(resDequeue1)
print(resDequeue2)

# Results of enqueue operation, first the given ADT, second our ADT
# [0.0004517100000001051, 0.0037792409999999332, 0.009572161000000134, 0.01834293099999984, 0.03222952000000001,
#  0.08748927000000073, 0.06595330000000033, 0.08843118100000069, 0.11814429900000079, 0.14256165600000514]
# [0.00026156499999996363, 0.00032741999999985616, 0.00026249200000005857, 0.0002634200000000142, 0.0002675939999998711,
#  0.00047582599999973496, 0.00025738999999980194, 0.00025739100000166104, 0.0002750139999996293, 0.0002578540000044427]
# Results of dequeue operation, first the given ADT, second our ADT
# 0.00025136200000019926
# 0.04351762099999945

