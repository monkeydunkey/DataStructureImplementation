# This one is an implementation with tail

class node(object):
    def __init__(self, value = None, Next = None):
        self.value = value
        self.Next = Next


class linkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addLast(self, value):
        self.size += 1
        if self.head is None:
            self.head  = node(value)
            self.tail = self.head
        else:
            self.tail.Next = node(value)
            self.tail = self.tail.Next

    def addFirst(self, value):
        self.size += 1
        nodeObj = node(value)
        nodeObj.Next = self.head
        if self.head is None:
            self.tail = nodeObj
        self.head = nodeObj

    def getLast(self):
        nodeObj = self.head
        while nodeObj.Next is not self.tail:
            nodeObj = nodeObj.Next
        return nodeObj
    
    def removeLast(self):
        if self.head is None:
            return 'List is empty'
        size -= 1
        if self.head is self.tail:
           self.head = None
           del self.tail
           self.tail = None

        nodeObj = self.getLast()
        nodeObj.next = None
        del self.tail
        self.tail = NodeObj

    def getSize(self):
        return self.size

    def getFirst(self):
        return self.head.value if self.head is not None else "The list is empty"

    def getLast(self):
        retun self.tail.value if self.head is not None else "The list is empty"

