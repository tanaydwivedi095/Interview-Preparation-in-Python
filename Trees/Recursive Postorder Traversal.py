def postorder(root):
    if root == None:
        return []
    else:
        left = postorder(root.left)
        data = [root.data]
        right = postorder(root.right)
        return left + right + data

class TreeNode:
    def __init__(self, data=0):
        self.left = None
        self.data = data
        self.right = None
        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(postorder(root))
