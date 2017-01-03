## an implementation of generic tree node

class treeNode(object):
    # n: The max number of children a single node can have
    def __init__(self, n, value):
        self.value = value
        for i in range(n):
            self['child'+str(i+1)] = None;

