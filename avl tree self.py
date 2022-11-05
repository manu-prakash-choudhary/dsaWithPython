class BinarySearchTreeNode:
    def __init__(self,key) :
        self.left = None
        self.right  = None
        self.data = key
        self.height = 1

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
        
        self.height = 1+max(self.right.get_height(),self.left.get_height())

        
    def inorder_traversal(self):
        elements = []
        
        if self.left :
            elements +=self.left.inorder_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements+=self.right.inorder_traversal()

        return elements

    def get_height(self):
        if not self:
            return 0
        
        return self.height
    