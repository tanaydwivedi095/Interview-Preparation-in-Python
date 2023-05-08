class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def checkIdentical(root1, root2):
    if root1==None and root2==None:
        return True
    elif root1==None or root2==None:
        return False
    else:
        if root1.val != root2.val:
            return False
        temp1 = checkIdentical(root1.left, root2.left)
        temp2 = checkIdentical(root1.right, root2.right)
        return temp1 and temp2
    
if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(2)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    root1.right.right.right = TreeNode(6)
    
    root2 = TreeNode(3)
    root2.left = TreeNode(2)
    root2.right = TreeNode(4)
    root2.left.left = TreeNode(1)
    root2.right.right = TreeNode(5)
    root2.right.right.right = TreeNode(6)
    
    print(checkIdentical(root1, root2))
