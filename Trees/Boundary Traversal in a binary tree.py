class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def leftBoundary(root):
    queue = [root]
    res = []
    while queue:
        currNode = queue.pop()
        if currNode!=None:
            res.append(currNode.val)
            if root.left!=None:
                queue.append(currNode.left)
            elif root.right!=None:
                queue.append(currNode.right)
    return res

def rightBoundary(root):
    queue = [root]
    res = []
    while queue:
        currNode = queue.pop(0)
        if currNode!=None:
            res.append(currNode.val)
            if root.right!=None:
                queue.append(currNode.right)
            elif root.left!=None:
                queue.append(currNode.left)
    return res
        
def leafBoundary(root, res=[]):
    if root==None:
        return res
    else:
        if root.left==None and root.right==None:
            res.append(root.val)
        left = leafBoundary(root.left, res)
        right = leafBoundary(root.right, res)
        return res
    
def boundaryTraversal(root):
    left = leftBoundary(root)
    right = rightBoundary(root)
    leaf = leafBoundary(root)
    res = []
    for i in range(0,len(left)):
        res.append(left[i])
    for i in range(1, len(leaf)):
        res.append(leaf[i])
    for i in range(len(right)-2, 0, -1):
        res.append(right[i])
    return res
        
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(8)
    print(boundaryTraversal(root))
