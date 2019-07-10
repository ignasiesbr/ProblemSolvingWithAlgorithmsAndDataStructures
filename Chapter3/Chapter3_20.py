# 20. Ordered List.

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = "["
        current = self.head
        size = self.size()
        for i in range(size - 1):
            s = s + str(current.getData()) + ", "
            current = current.getNext()
        s = s + str(current.getData())
        s = s + "]"
        return s

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item):
        current  = self.head
        previous =  None
        stop = False
        found = False
        while current != None and not stop:
            if current.getData() == item:
                stop = True
                found = True
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def index(self, item):
        current = self.head
        stop = False
        found = False
        count = 0
        while current is not None and not stop:
            if current.getData() == item:
                stop = True
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
                count = count + 1
        if found:
            return count

    def pop(self):
        current = self.head
        previous = None
        size = self.size()
        for i in range(size - 1):
            previous = current
            current = current.getNext()
        popped = current.getData()
        if previous is None:
            self.head = None
            return popped
        else:
            previous.setNext(None)
            return popped

    def popPos(self, pos):
        current = self.head
        previous = None
        for i in range(pos):
            previous = current
            current = current.getNext()
        popped = current.getData()
        if previous is None:
            self.head = current.getNext()
            return popped
        else:
            previous.setNext(current.getNext())
            return popped



mylist = OrderedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)

