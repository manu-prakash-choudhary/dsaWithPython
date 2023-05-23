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
                # self.avl_balance(data)   uncomment these two lines if you want avl trees.
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def get_height(self,root):
        a,b=0,0
        
        if root is None:
            return 0
        while root.left or root.right:  
            if root.right:
                a += 1
                root = root.right
            else:
                b += 1
                root = root.left
        # if a==b:
        #     return True
        # else:
        #     return False
        # print(a, b)
        return max(a,b)+1

def build_tree(element):
    BT = BinarySearchTreeNode(element[0])
    for i in range(1,len(element)):
        BT.add_child(element[i])
    return BT
#  list with values 5 3 8 1 4 7 10
n = int(input())
element = list(map(int,input().split()))
my_list = build_tree(element)
# check if tree is balanced
if my_list.right:
    right_height = my_list.get_height(my_list.right)
    left_height = 0
    if my_list.left:
        left_height = my_list.get_height(my_list.left)
    if abs(right_height - left_height) > 1:
        print("The binary tree is not height-balanced")
    else:
        print("The binary tree is height-balanced")

elif my_list.left:
    right_height = 0
    if my_list.right:
        right_height = my_list.get_height(my_list.right)
    left_height = my_list.get_height(my_list.left)
    if abs(right_height - left_height) > 1:
        print("The binary tree is not height-balanced")
    else:
        print("The binary tree is height-balanced")


if my_list.left:
    right_height = 0
    if my_list.right:
        right_height = my_list.get_height(my_list.right)
    left_height = my_list.get_height(my_list.left)
    if abs(right_height - left_height) > 1:
        print("Not balanced")
    
else:
    left_height = 0

# print(my_list.get_height(my_list))