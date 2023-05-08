class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def inorder(root):
    stack = []
    res = []
    node = root
    while True:
        if node!=None:
            stack.append(node)
            node = node.left
        else:
            if len(stack)==0:
                break
            node = stack.pop()
            res.append(node.val)
            node = node.right
    return res
        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(inorder(root))
