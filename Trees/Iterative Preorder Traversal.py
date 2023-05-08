class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def preorder(root):
    stack = [root]
    res = []
    while stack:
        currNode = stack.pop(-1)
        if currNode!=None:
            stack.append(currNode.right)
            stack.append(currNode.left)
            res.append(currNode.val)
    return res
        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(preorder(root))
