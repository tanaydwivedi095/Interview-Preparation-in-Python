class TreeNode:
    def __init__(self, data=0):
        self.left = None
        self.data = data
        self.right = None
        
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(7)
    print(root.data)
    print(root.left.data)
    print(root.right.data)
