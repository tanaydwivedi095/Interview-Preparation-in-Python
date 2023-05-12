class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def zigzag(root):
    result = []
    if root==None:
        return result
    else:
        queue = [root]
        leftToRight = True
        while queue:
            size = len(queue)
            row = []
            for i in range(0,size):
                node = queue.pop(0)
                row.append(node.val)
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            leftToRight = not leftToRight
            result.append(row)
        return result
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    print(zigzag(root))
