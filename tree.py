class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
def max(root):
    if root is None:
        return 0
 
    return 1 + max(max(root.left), max(root.right))