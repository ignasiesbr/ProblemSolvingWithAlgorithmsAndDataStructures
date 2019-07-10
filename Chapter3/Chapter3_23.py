# implement a queue using linked lists
from Chapter3_13to19 import UnorderedList


class Queue:

    def __init__(self):
        self.items = UnorderedList()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.length()

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())
print(q.size())
print(q.isEmpty())