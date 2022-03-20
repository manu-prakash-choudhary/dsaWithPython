
"""
                                            Binary Tree
Binary Tree are of three types full,complete and strict
example of application is huffman coding tree.

 - > finding minimum and maximum - Traverse only left part of subtrees to find minimum and traverse only right part for finding maximum

 ->  



"""


class BinarySearchTreeNode:
    def __init__(self,key) :
        self.left = None
        self.right  = None
        self.data = key
    

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self,value):
        
        if self.data==value:
            return True

        if self.data>value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if self.data<value:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def inorder_traversal(self):
        elements = []
        
        if self.left :
            elements +=self.left.inorder_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements+=self.right.inorder_traversal()

        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

def build_tree(element):
    BT = BinarySearchTreeNode(element[0])

    for i in range(1,len(element)):
        BT.add_child(element[i])

    return BT

    

element = [17,4,9,20,18,345,22,11]
my_list = build_tree(element)
print(my_list.inorder_traversal())
print(my_list.search(34))
print(my_list.find_min())
print(my_list.find_max())


