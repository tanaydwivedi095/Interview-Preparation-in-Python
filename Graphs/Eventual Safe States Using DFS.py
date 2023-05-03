def dfs(node):
    visited[node] = 1
    pathVisited[node] = 1
    check[node] = 0
    for neighbour in adjList[node]:
        if visited[neighbour] == 0:
            if dfs(neighbour) == True:
                return True
        elif pathVisited[neighbour] == 1:
            check[node] = 0
            return True
    check[node] = 1
    pathVisited[node] = 0
    return False

if __name__ == "__main__":
    n = 5
    adjList = {
        0:[1],
        1:[2],
        2:[3],
        3:[4],
        4:[]
    }
    visited = [0 for i in range(0,n)]
    pathVisited = [0 for i in range(0,n)]
    check = [0 for i in range(0,n)]
    for i in range(0,n):
        if visited[i]==0:
            dfs(i)
    safeNodes = []
    for i in range(0,n):
        if check[i]==1:
            safeNodes.append(i)
    print(safeNodes)
