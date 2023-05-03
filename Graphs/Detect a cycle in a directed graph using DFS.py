def dfs(node):
    visited[node] = 1
    pathVisited[node] = 1
    for neighbour in adjList[node]:
        if visited[neighbour]==0:
            if dfs(neighbour) == True:
                return True
        elif (pathVisited[neighbour]):
            return True
    pathVisited[node] = 0
    return False
    
if __name__ == "__main__":
    adjList = {
            0:[1],
            1:[2],
            2:[3],
            3:[4,7],
            4:[5],
            5:[6],
            6:[],
            7:[5],
            8:[9],
            9:[10],
            10:[8]
        }
    flag = 0
    visited = [0 for i in range(11)]
    pathVisited = [0 for i in range(11)]
    for i in range(0,11):
        if visited[i] == 0:
            if dfs(i) == True:
                print("A cycle exists")
                flag = 1
                break
    if flag==0:
        print("No cycle exists")
