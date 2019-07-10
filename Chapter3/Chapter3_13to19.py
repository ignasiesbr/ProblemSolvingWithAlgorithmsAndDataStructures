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

class UnorderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.size = self.size + 1

    def length(self):
        return self.size

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    #Ex 14.
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                return
            elif current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None :
            self.head = current.getNext()
            self.size = self.size - 1
        else:
            previous.setNext(current.getNext())
            self.size = self.size - 1

    #16 and 17
    def __str__(self):
        s = "["
        current = self.head
        for i in range(self.size - 1):
            s = s + str(current.getData()) + ", "
            current = current.getNext()
        s = s + str(current.getData())
        s = s + "]"
        return s
    #18
    def append(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
            self.size = self.size + 1
        else:
            current = self.head
            for i in range(self.size - 1):
                current = current.getNext()
            current.setNext(temp)
            self.size = self.size + 1

    def index(self, value):
        count = 0
        current = self.head
        for i in range(self.size):
            if current.getData() == value:
                return count
            else:
                current = current.getNext()
                count = count + 1

    def pop(self):
        current = self.head
        previous = None
        for i in range(self.size - 1):
            previous = current
            current = current.getNext()
        d = current.getData()
        if previous is None:
            self.head = None
            self.size = 0
            return d
        else:
            previous.setNext(current.getNext())
            self.size = self.size - 1
            return d

    def popPos(self, pos):
        current = self.head
        previous = None
        for i in range(pos):
            previous = current
            current = current.getNext()
        popped = current.getData()
        if previous is None:
            self.head = current.getNext()
            self.size = self.size - 1
            return popped
        else:
            previous.setNext(current.getNext())
            self.size = self.size - 1
            return popped

    def insert(self, pos, item):
        temp = Node(item)
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if pos == 0:
                found = True
            else:
                previous = current
                current = current.getNext()
                pos = pos - 1

        if found:
            temp.setNext(current)
            previous.setNext(temp)
            self.size = self.size + 1
        else:
            self.append(item)

    #19.
    #Returns a list from start to stop(not included)
    def slice(self, start, stop):
        res = UnorderedList()
        count = 0
        int = range(start,stop)
        current = self.head
        for i in int:
            if count in int:
                res.append(current.getData())
            count = count + 1
            current = current.getNext()
        return res





l = UnorderedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
