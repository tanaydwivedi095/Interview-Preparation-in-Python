def bfs(src, adj):
    visited[src] = 1
    q = [(src, -1)]
    while q:
        node, parent = q.pop(0)
        for neighbour in adj[node]:
            if visited[neighbour] == 0:
                visited[neighbour] = 1
                q.append((neighbour, node))
            elif parent != neighbour:
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
    edges = [[1,2],[2,3],[3,4],[4,5]]
    adjList = adjListCreator(edges,n)
    visited = [0 for i in range(n+1)]
    for i in range(0,n+1):
        if visited[i]==0:
            result = bfs(i, adjList)
            if result:
                print("There exists a cycle")
                break
    if result==False:
        print("There is no cycle in the graph")
    
