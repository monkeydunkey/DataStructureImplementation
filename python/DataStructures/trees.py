## an implementation of generic tree node

class treeNode(object):
    # n: The max number of children a single node can have
    def __init__(self, n, value):
        self.value = value
        #self.child1 = None
        #self.child2 = None
        for i in range(n):
           setattr(self,'child'+str(i+1), None)

