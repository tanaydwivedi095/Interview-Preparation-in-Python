class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def postorder(root):
    stack1 = [root]
    res = []
    while stack1:
        currNode = stack1.pop(-1)
        if currNode!=None:
            res.append(currNode.val)
            if currNode.left != None:
                stack1.append(currNode.left)
            if root.right != None:
                stack1.append(currNode.right)
    return res
        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(postorder(root))
