## Queue implementation using singly linked list

import linkedList as ll

class queue(object):
    def __init__ (self):
        self.ptr = None;
        self.head = None;

    def enqueue(self, values):
        if not isinstance(values, list):
            values = [values]
        for value in values: 
            if self.head is None:
                self.head = ll.singleNode(value)
                self.ptr = self.head
            else:
                self.ptr.next = ll.singleNode(value);
                self.ptr = self.ptr.next;

    def dequeue(self):
        retValue = None
        if self.head is None:
            return 'Queue is empty'
        else:
            retValue = self.head.value
            if head is ptr:
                head = None
                ptr = None
            else:
                head = head.next;

            return retValue

    def peek(self):
        if head is not None:
            return self.head.value;
        else:
            return 'Queue is empty'

