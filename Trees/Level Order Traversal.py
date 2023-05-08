class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def levelOrderTraversal(root):
    queue = [root]
    levels = []
    while queue:
        currNode = queue.pop(0)
        if currNode!=None:
            queue.append(currNode.left)
            queue.append(currNode.right)
            levels.append(currNode.val)
    return levels

        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(levelOrderTraversal(root))
