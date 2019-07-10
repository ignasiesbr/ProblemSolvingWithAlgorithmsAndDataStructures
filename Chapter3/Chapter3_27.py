#implement a double linked list.

class Node:

    def __init__(self, item):
        self.next = None
        self.back = None
        self.data = item

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getBack(self):
        return self.back

    def setData(self, d):
        self.data = d

    def setNext(self, item):
        self.next = item

    def setBack(self, item):
        self.back = item



class DoubleList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        s = "["
        current = self.head
        for i in range(self.size() - 1):
            s = s + str(current.getData()) + ", "
            current = current.getNext()
        s = s + str(current.getData()) + "]"
        return s

    def add(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.head.setBack(temp)
            temp.setNext(self.head)
            self.head = temp

    def append(self, item):
        temp = Node(item)
        if self.tail is None:
            self.tail = temp
            self.head = temp
        else:
            oldtail = self.tail
            self.tail.setNext(temp)
            self.tail = temp
            self.tail.setBack(oldtail)

    def size(self):
        current = self.head
        len = 0
        while current is not None:
            current = current.getNext()
            len = len + 1
        return len


    # aux function to check if the back links work properly
    def checkReverse(self):
        current = self.tail
        while current is not None:
            print(current.getData())
            current = current.getBack()



    #index

    #pop




l = DoubleList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)


