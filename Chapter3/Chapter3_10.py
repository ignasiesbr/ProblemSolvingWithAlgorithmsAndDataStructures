# Radix sorting machine
# assume that every number have the same digits.
# to solve the assumption, pad with 0 the number before radix sort it.

from pythonds.basic.queue import Queue

def radixSorter(lon):
    mainBin = Queue()
    digList = []
    for i in range(10):
        digList.append(Queue())

    res = []
    #pass all the lon items into the mainBin:
    for n in lon:
        mainBin.enqueue(n)

    for i in [1, 0]:
        while not mainBin.isEmpty():
            n = mainBin.dequeue()
            digList[int(str(n)[i])].enqueue(n)

        for queue in digList:
            while not queue.isEmpty():
                mainBin.enqueue(queue.dequeue())

    #return the queue as a list of numbers
    while not mainBin.isEmpty():
        res.append(mainBin.dequeue())
    return res

lon = [23,45,55,12,76,56,88]
print(radixSorter(lon))









