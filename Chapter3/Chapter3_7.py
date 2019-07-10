#7. Implement a queue that have O(1) (average) on enqueue and dequeue.

from pythonds.basic.stack import Stack

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        if self.outbox.isEmpty():
            while (not self.inbox.isEmpty()):
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()

    
