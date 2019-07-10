#Implement the Queue ADT, rear queue is end of the list

class Queue2:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def __str__(self):
        s = ""
        for item in self.items:
            s = s + str(item) + ", "
        return s
