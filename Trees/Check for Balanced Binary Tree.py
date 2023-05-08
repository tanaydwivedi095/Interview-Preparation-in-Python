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
        if left==False:
            return -1
        right = maxDepth(root.left)
        if right == False:
            return -1
        if abs(left-right)>1:
            return -1
    return max(left,right)+1

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    print(True if maxDepth(root)!=-1 else False)
