def bfs(adjList, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        currNode = queue.pop(0)
        for neighbour in adjList[currNode]:
            if visited[neighbour]==False:
                visited[neighbour] = True
                queue.append(neighbour)
    return visited

def adjListCreator(adjMatrix):
    adjList = {}
    for i in range(0,len(adjMatrix)):
        for j in range(0,len(adjMatrix[i])):
            if adjMatrix[i][j] == 1:
                if i not in adjList:
                    adjList[i] = [j]
                else:
                    adjList[i].append(j)
    return adjList

def numberOfProvinces(adjList):
    visited = [False for i in range(0,len(adjList))]
    res = 0
    for i in range(0,len(visited)):
        if visited[i] == False:
            visited = bfs(adjList, i, visited)
            res += 1
    return res

if __name__ == "__main__":
    adjMatrix = [[1,0,0],[0,1,0],[0,0,1]]
    adjList = adjListCreator(adjMatrix)
    print(numberOfProvinces(adjList))
    
