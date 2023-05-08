def inorder(root):
    if root == None:
        return []
    else:
        left = inorder(root.left)
        data = [root.data]
        right = inorder(root.right)
        return left + data + right

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
    print(inorder(root))
