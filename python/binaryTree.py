from trees import treeNode

class binaryNode(treeNode):

    def __init__(self, value):
        treeNode.__init__(self, 2, value)
        self.left = self.child1
        self.right = self.child2


class binaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = binaryNode(value)
        else
            tmp = self.root
            parentNode = self.root
            while tmp is not None:
                parentNode = tmp
                if tmp.value > value:
                    tmp = tmp.left
                else: 
                    tmp = tmp.right
            if parentNode.value > value:
                parentNode.left = binaryNode(value)
            else:
                parentNode.right = binaryNode(value)

    # Checks if a value is present in the tree or not
    def contains(self, value):
        if self.root is None:
            return 'The tree is empty'
        else:
            tmp = self.root
            while tmp is not None:
                if tmp.value == value:
                    return True
                else:
                    if tmp.value > value:
                        tmp = tmp.left
                    else:
                        tmp = tmp.right
            return False
