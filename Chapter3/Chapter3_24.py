# Implement a deque with linked lists
from Chapter3_13to19 import UnorderedList


class Deque:

    def __init__(self):
        self.items = UnorderedList()

    def __str__(self):
        return self.items.__str__()

    def addFront(self, item):
        self.items.add(item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.popPos(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.length()


d  = Deque()
d.addFront(1)
d.addFront(2)
d.addRear(1)
d.addRear(2)
print(d.removeFront())
print(d.removeRear())