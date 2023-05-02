def dfs(source, parent):
    visited[source] = 1
    for neighbour in adjList[source]:
        if visited[neighbour] == 0:
            if dfs(neighbour, source):
                return True
        elif neighbour!=parent:
            return True
    return False
    
def adjListCreator(edges,n):
    adjList = {}
    for i in range(0,n+1):
        adjList[i] = []
    for edge in edges:
        start, end = edge
        adjList[start].append(end)
        adjList[end].append(start)
    return adjList

if __name__ == "__main__":
    n = 5
    edges = [[1,2],[2,3],[3,4],[4,1]]
    adjList = adjListCreator(edges,n)
    visited = [0 for i in range(0,n+1)]
    for i in range(0,n+1):
        if visited[i] == 0:
            result = dfs(i, adjList)
            if result == True:
                print("The graph consists a cycle")
                break
    if result == False:
        print("The graph does not consist a cycle")
