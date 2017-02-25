## stack implementation using singly linked linked list

import linkedList as ll

class stack(object):
    def __init__ (self):
        self.ptr = None;
        self.head = None;

    def push(self, values):
        if not isinstance(values, list):
            values = [values]
        for value in values: 
            if self.head is None:
                self.head = ll.singleNode(value)
                self.ptr = self.head
            else:
                tmp = ll.singleNode(value);
                tmp.next = self.ptr;
                self.ptr = tmp

    def pop(self):
        retValue = None
        if self.ptr is None:
            return 'Stack is empty'
        else:
            retValue = self.ptr.value
            if self.head is self.ptr:
                self.ptr = None
                self.head = None
            else:
                self.ptr = self.ptr.next;

            return retValue

    def peek(self):
        return self.ptr.value if self.ptr is not None else 'Stack is empty';

class MaxStack(object):

    # initialize an empty list
    def __init__(self):
        self.items = []
        self.auxStack = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)
        if len(self.auxStack) == 0 or self.auxStack[-1] < item:
            self.auxStack.append(item)
        else:
            self.auxStack.append(self.auxStack[-1])

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        self.auxStack.pop()
        return self.items.pop()

    #get the max item
    def getMax(self):
        return None if len(self.auxStack) == 0 else self.auxStack[-1]
    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
