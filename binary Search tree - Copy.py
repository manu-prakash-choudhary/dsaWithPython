
"""
                                            Binary Tree
Binary Tree are of three types full,complete and strict
example of application is huffman coding tree.

 -> inserting a node : if we want to insert a value 12 then we have check if current node has further right or left subtree if not then we will compare current node value with the value we want to insert

 - > finding minimum and maximum - Traverse only left part of subtrees to find minimum and traverse only right part for finding maximum

 ->  deleting a node from binary search tree.
        There are two ways to do that 
            1) using left subtree and right subtree if we will traverse till we find the node to be deleted(self Node) Now using left subtree method we will look for maximum value in left subtree and will set self.data= maximum and then we will apply delete method again(i.e., recursion) till we reach the leaf node so that we can remove that peacfully

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

-> BFS vs DFS 
        BFS(or level order traversal) - visit row wise
        DFS : visit column wise column will come first.



AVL TREE
->  AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes. 

        Why AVL Trees? 
        Most of the BST operations (e.g., search, max, min, insert, delete.. etc) take O(h) time where h is the height of the BST. The cost of these operations may become O(n) for a skewed Binary tree. If we make sure that height of the tree remains O(Logn) after every insertion and deletion, then we can guarantee an upper bound of O(Logn) for all these operations. The height of an AVL tree is always O(Logn) where n is the number of nodes in the tree.

    
-> AVL tree insertion  have four cases which one to use will depend on where the new node has been inserted 
    https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
    Lets say the node inserted is w, now from w traverse to the unbalanced node, now there can be four cases of unbalancing  which can handled as follows

    lets take w be the inserted node, y be the node in between the unbalanced node and inserted node, and z be the unbalanced node.
    
    If the structure of unbalanced tree is left left position then rotating it to the right from z node will make the tree balanced.
    If the structure of unbalanced tree is right right position then rotating it to the left from z node will make the tree balanced.
    If the structure of unbalanced tree is left right position then rotating it to the left first from the y node and then rotating to the right from z node.
    If the structure of unbalanced tree is right left position then rotating it to the right first from the y node and then rotating to the left from z node.


--> Applications of Binary tree - https://www.geeksforgeeks.org/applications-of-minimum-spanning-tree/
    1. Minimum Spanning Tree problem can be solved using Binary tree
    2. Minimum Bottleneck Spanning Tree(MSBT) - The minimum bottleneck spanning tree in an undirected graph is a tree whose most expensive edge is as minimum as possible
            All minimum spanning trees are minimum bottleneck spanning tree but vice versa is not True
    3.LDPC (low density parity correction)  - It is used to transmit signals over noisy channels with noise threshold value as close as possible to theoritical threshold value also known as shannon threshold.
    


---> BFS and DFS
        . BFS and DFS(Inorder, Preorder and Postorder) all four traversals require O(n) time 
        . Extra Space required for Level Order Traversal is O(w) where w is maximum width of Binary Tree. In level order traversal, queue one by one stores nodes of different level.
        . Extra Space required for Depth First Traversals is O(h) where h is maximum height of Binary Tree. In Depth First Traversals, stack (or function call stack) stores all ancestors of a node.


--> Binary Tree (Array implementation) - It is tree representing technique using array such that array indexes are values in tree nodes and array values give the parent node of that particular index (or node). The value of the root node index would always be -1 as there is no parent for root.

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

    def inorder_traversal(self):  #inorder == (left_node->root_node->right_node)
        elements = []
        if self.left :
            elements +=self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder_traversal()
        return elements

    def preorder_traversal(self):   #preorder == root_node-> left_node -> right_node
        elements = []
        elements.append(self.data)
        if self.left :
            elements +=self.left.inorder_traversal()
        if self.right:
            elements+=self.right.inorder_traversal()
        return elements

    def postorder_traversal(self):   #postorder ==  left_node -> right_node -> root_node
        elements = []
        if self.left :
            elements +=self.left.inorder_traversal()
        if self.right:
            elements+=self.right.inorder_traversal()
        elements.append(self.data)
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

    


    



    def get_height(self):
        a,b=1,1
        while self.left or self.right:  
            if self.right:
                a += 1
                self = self.right
            else:
                b += 1
                self = self.left
        return max(a,b)+1
        

    def print_current_level(self,root,level):
        if root is None:
            return None
        if level==1:
            print(root.data,end=" -> ")
        elif level>1:
            self.print_current_level(root.left,level-1)
            self.print_current_level(root.right,level-1)

        
    def bfs(self):
        h = self.get_height()
        print("bfs => ",end="")
        for i in range(1,h+1):
            self.print_current_level(self,i)
        print("None")
    
    # binary tree array implementation

                

def build_tree(element):
    BT = BinarySearchTreeNode(element[0])

    for i in range(1,len(element)):
        BT.add_child(element[i])

    return BT



    

element = [17,4,9,20,18,345,22,11]    
my_list = build_tree(element)
print(my_list.inorder_traversal()) #this will be sorted list.


# my_list.bfs()
# print("Inorder =>",my_list.preorder_traversal())
# print("Postorder =>",my_list.postorder_traversal())
# print(my_list.dfs())
# print(my_list.get_height())
# print(my_list.search(34))

# print(my_list.find_min())
# print(my_list.find_max())

# my_list.insertion_list(14)
# print("After -> ", my_list.inorder_traversal())
# print(my_list.inorder_traversal())
# my_list.delete(4)


