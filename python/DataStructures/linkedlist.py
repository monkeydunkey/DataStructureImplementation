## Linked list implementation in python

## Implementation of singly linked, linked list
class singleNode(object):
    def __init__(self, value = None, next = None):
        self.value = value;
        self.next = next;
    def __str__(self):
        return str(self.value)

## Implementation of doubly linked, linked list 
class doubleNode(object):
    def __init__(self, value = None, next = None, prev = None):
        self.value = value;
        self.next = next;
        self.prev = prev;

    def __str__(self):
        return str(self.value)
