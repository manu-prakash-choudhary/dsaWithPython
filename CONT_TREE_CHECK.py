#Python Program to check continous tree or not

class newNode():
    def __init__(self,key) :
        self.left = None
        self.right  = None
        self.data = key
def treeContinuous(root):
    if not root:
        return True
    if root.left:
        if not abs(root.data-root.left.data)==1:
            return False
    if root.right:
        if not abs(root.data-root.right.data)==1:
            return False
    if treeContinuous(root.left) and treeContinuous(root.right):
        return True

# Driver code
if __name__ == '__main__':
    root =  newNode(7)
    root.left = newNode(6)
    root.right = newNode(8)
    root.left.left = newNode(5)
    root.left.right = newNode(7)
    root.right.right = newNode(7)
    
    print(treeContinuous(root))
