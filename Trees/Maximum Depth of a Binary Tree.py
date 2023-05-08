class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def maxDepth(root):
    if root==None:
        return 0
    else:
        left = maxDepth(root.left)
        right = maxDepth(root.left)
        return max(left,right) + 1
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(maxDepth(root))
