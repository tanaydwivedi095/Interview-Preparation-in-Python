class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def maxSum(root):
    if root==None:
        return 0
    else:
        left = maxSum(root.left)
        right = maxSum(root.right)
        return max(left, right) + root.val
        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    print(maxSum(root))
