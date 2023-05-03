def dfs(node, currColor):
    color[node] = currColor
    for neighbour in adjList[node]:
        if color[neighbour] == -1:
            if dfs(neighbour, int(not(currColor))) == False:
                return False
            elif color[neighbour] == currColor:
                return False
    return True
    
if __name__ == "__main__":
    adjList = {
        0:[1],
        1:[2,4,5],
        2:[3],
        3:[7],
        4:[5,2,3,4,5,6,7],
        5:[6],
        6:[7],
        7:[8],
        8:[1]
    }
    n=8
    color = [-1 for i in range(0,n+1)]
    for i in range(0,n+1):
        if color[i]==-1:
            if dfs(i,0) == False:
                print(False)
                break
    print(color)
    print(True)
