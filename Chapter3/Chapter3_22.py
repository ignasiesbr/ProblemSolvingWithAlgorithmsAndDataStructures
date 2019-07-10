# Implement a stack using linked lists.

from Chapter3_13to19 import UnorderedList

class Stack:
    def __init__(self):
        self.items = UnorderedList()

    def __str__(self):
        return self.items.__str__()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        current = self.items.head
        for i in range(self.items.length() - 1):
            current = current.getNext()
        return current.getData()

    def size(self):
        return self.items.length()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.pop())
print(s.size())