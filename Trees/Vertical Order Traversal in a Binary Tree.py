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
        if node.left != None:
            queue.append((node.left, x-1, y+1))
        if node.right != None:
            queue.append((node.right, x+1, y+1))
        if x not in levelMap:
            levelMap[x] = {y:[node.val]}
        else:
            temp = levelMap[x]
            if y not in temp:
                levelMap[x][y] = [node.val]
            else:
                levelMap[x][y].append(node.val)
    for k,v in levelMap.items():
        lst = sorted(v.values())
        levelMap[k] = lst
    res = []
    lst = list(levelMap.values())
    for i in range(0,len(lst)):
        temp = []
        for j in range(0,len(lst[i])):
            for k in range(0,len(lst[i][j])):
                temp.append(lst[i][j][k])
        res.append(temp)
    return res
    
    
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
    print(verticalOrder(root))
