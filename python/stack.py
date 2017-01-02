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

