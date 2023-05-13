class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.val = val
        self.right = None
        
def verticalOrder(root):
    levelMap = dict()
    # (node, x, y)
    queue = [(root, 0, 0)]
    while queue:
        currNode = queue.pop(0)
        node, x, y = currNode
        print(node.val, end=" ")
        if node.left != None:
            queue.append((node.left, x-1, y+1))
        if node.right != None:
            queue.append((node.right, x+1, y+1))
        if y not in levelMap:
            levelMap[y] = {x:node.val}
        else:
            levelMap[y][x] = node.val
    for k,v in levelMap.items():
        lst = sorted(v.values())
        levelMap[k] = lst
    return list(levelMap.values())
    
    
def treeCreator():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(10)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    return root

if __name__ == "__main__":
    root = treeCreator()
    print(verticalOrder(root))
