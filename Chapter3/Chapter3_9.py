#9. Modify the hot potato simulation to allow for a randomly chosen counting value.

from pythonds.basic import Queue
import random
def hotPotato(namelist):

    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        n = random.randint(1, 10)
        for i in range(n):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"]))

