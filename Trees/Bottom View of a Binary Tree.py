class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def BottomViewOrder(root):
    levelMap = dict()
    queue = [(root, 0)]
    while queue:
        currNode = queue.pop(0)
        node, x = currNode
        if node.left != None:
            queue.append((node.left, x-1))
        if node.right != None:
            queue.append((node.right, x+1))
        levelMap[x] = node.val
    return list(levelMap.values())
    
    
def treeCreator():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(10)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(10)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    return root

if __name__ == "__main__":
    root = treeCreator()
    print(BottomViewOrder(root))
