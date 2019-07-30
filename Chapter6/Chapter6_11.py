# Implement PriorityQueue

from Chapter6_10 import BinHeap

class PriorityQueue(BinHeap):

    def enqueue(self, item):
        self.insert(item)

    def dequeue(self):
        self.delMax()

pqueue = PriorityQueue()
pqueue.enqueue(2)

