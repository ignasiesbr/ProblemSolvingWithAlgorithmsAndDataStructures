# Implement Max Heap
class BinHeap: # Max Heap

    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def insert(self, k):
        self.heapList.append(k)
        self.size = self.size + 1
        self.percUp(self.size)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i // 2] < self.heapList[i]:
                self.heapList[i // 2], self.heapList[i] = self.heapList[i], self.heapList[i // 2]
            i = i // 2

    def maxChild(self, i):
        if (i * 2) + 1 > self.size:
            return (i*2)
        else:
            if self.heapList[i*2 + 1] > self.heapList[i*2]:
                return (i*2 + 1)
            else:
                return (i*2)

    def percDown(self, i):
        while (i*2) <= self.size:
            mc = self.maxChild(i)
            if self.heapList[mc] > self.heapList[i]:
                self.heapList[mc], self.heapList[i] = self.heapList[i], self.heapList[mc]
            i = mc

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heapList = [0] + alist
        while i > 0:
            self.percDown(i)
            i = i - 1

    def __str__(self):
        return str(self.heapList)

    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.percDown(1)
        return retval


h = BinHeap()
h.buildHeap([5,1,10,4])
