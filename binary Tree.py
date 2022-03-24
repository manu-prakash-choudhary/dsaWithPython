
"""
                                            Binary Tree
Binary Tree are of three types full,complete and strict
example of application is huffman coding tree.

 -> inserting a node : if we want to insert a value 12 then we have check if current node has further right or left subtree if not then we will compare current node value with the value we want to insert

 - > finding minimum and maximum - Traverse only left part of subtrees to find minimum and traverse only right part for finding maximum

 ->  deleting a node
        There are two ways to do that 1) using left subtree and right subtree if

        we will traverse till we find the node to be deleted(self Node)
        Now using left subtree method we will look for maximum value in left subtree and will set self.data= maximum
        and then we will apply delete method again(i.e., recursion) till we reach the leaf node so that we can remove that peacfully

        same with right subtree method except the fact that we will look for minimum value from right subtree




Below is some bull shit theory!

-> Handshake theorem
        Basically it tells about properties of Binary tree  mentioned below 
            -> Handshaking lemma is about an undirected graph. In every finite undirected graph, an even number of vertices will always have an odd degree. 
            -> Sum of degree of all vertices is twice the number of edges i.e., Σdeg(V) = 2|E|
            Number of leaf nodes is always one more than number of internal nodes with two children
            
            -> N'th Catalan numbers

-> Insertion in a binary tree
        -> To insert in a binary tree we will traverse the tree by comparing each node with value to be inserted.
        whenever we will reach the leaf node we will set self.data = value.





             

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

    def delete(self,value):

        if value<self.data:
            if self.left:
                self.left = self.left.delete(value)
            else:
                return None

        elif value>self.data:
            if self.right:
                self.right = self.right.delete(value)
            else:
                return None
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is  None: 
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.find_min()
            self.data = min_val
            self.right.delete(min_val)


    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def insertion_list(self,value):
        
        if self.data:
            if self.data>value:
                if self.left:
                    self.left.insertion_list(value)
                else:
                    self.left = BinarySearchTreeNode(value)
            
            elif self.data<value:
                if self.right:
                    self.right.insertion_list(value)
                else:
                    self.right = BinarySearchTreeNode(value)
            
            else:
                print("already exists")
                return
        else:
            self.data = value

        
                    
                


            

def build_tree(element):
    BT = BinarySearchTreeNode(element[0])

    for i in range(1,len(element)):
        BT.add_child(element[i])

    return BT



    

element = [17,4,9,20,18,345,22,11]
my_list = build_tree(element)
print('Before -> ',my_list.inorder_traversal())
# print(my_list.search(34))
# print(my_list.find_min())
# print(my_list.find_max())
my_list.insertion_list(14)
print("After -> ", my_list.inorder_traversal())


