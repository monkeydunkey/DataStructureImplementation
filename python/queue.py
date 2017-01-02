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
        if self.ptr is None:
            return 'Queue is empty'
        else:
            retValue = self.ptr.value
            tmp = self.head
            if tmp is self.ptr:
                self.ptr = None
                self.head = None
            else:
                while tmp.next is not self.ptr:
                    tmp = tmp.next
                    continue
                tmp.next = None
                self.ptr = tmp

            return retValue

    def peek(self):
        return self.ptr.value;

