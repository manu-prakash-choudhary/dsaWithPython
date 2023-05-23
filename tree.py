class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructTree(arr, root, i, n):
    if i < n:
        root = Node(arr[i])
        root.left = constructTree(arr, root.left, 2 * i + 1, n)
        root.right = constructTree(arr, root.right, 2 * i + 2, n)
    return root

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def diameter(root):
    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    ld = diameter(root.left)
    rd = diameter(root.right)

    return max(lh + rh + 1, max(ld, rd))

# Input space-separated elements to create a binary tree
arr = list(map(int, input().split()))

# Construct the binary tree
root = None
root = constructTree(arr, root, 0, len(arr))

# Calculate the diameter of the binary tree
print("Diameter of the binary tree:", diameter(root))
