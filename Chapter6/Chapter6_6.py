# Create a binary heap with limited heap size.

class BinaryHeapLimited:
    def __init__(self, limit):
        self.heap = [0]
        self.size = 0
        self.limit = limit

    def __str__(self):
        return str(self.heap[1:])

    def insert(self, k):
        self.heap.append(k)
        self.size = self.size + 1
        self.percUp(self.size)
        if self.size > self.limit:
            self.heap.pop()
            self.size = self.size - 1

    def percUp(self, i):
        while (i // 2) > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2

h = BinaryHeapLimited(6)
h.insert(1)
h.insert(3)
h.insert(4)
h.insert(5)
h.insert(6)





