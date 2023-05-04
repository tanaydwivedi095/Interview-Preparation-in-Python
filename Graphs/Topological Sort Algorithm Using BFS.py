def bfs(queue):
    while queue:
        currNode = queue.pop(0)
        result.append(currNode)
        for neighbour in adjList[currNode]:
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                queue.append(neighbour)
        
def inDegreeCreator(n,adjList):
    indegree = [0 for i in range(0,n)]
    for neighbours in adjList.values():
        for node in neighbours:
            indegree[node] += 1
    return indegree
        
def adjListCreator(n, edges):
    adjList = {i:[] for i in range(0,n)}
    for edge in edges:
        start, end = edge
        adjList[start].append(end)
    return adjList
    
if __name__ == "__main__":
    n = 6
    result = []
    edges = [[5,0],[4,0],[5,2],[4,1],[2,3],[3,1]]
    adjList = adjListCreator(n, edges)
    inDegree = inDegreeCreator(n, adjList)
    visited = [0 for i in range(0,n)]
    queue = []
    for i in range(0,n):
        if inDegree[i] == 0:
            queue.append(i)
    bfs(queue)
    print(result)
