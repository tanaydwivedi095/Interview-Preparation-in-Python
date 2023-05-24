from math import inf
from heapq import heappop, heappush

def prims(adjList, n):
    minHeap = []
    vis = [0 for i in range(n)]
    res=0
    heappush(minHeap, (0,0))
    while minHeap:
        wt, node = heappop(minHeap)
        if vis[node]==1:
            continue
        vis[node]=1
        res += wt
        for neighbour in adjList[node]:
            adjNode = neighbour[0]
            edW = neighbour[1]
            if not vis[adjNode]:
                heappush(minHeap, (edW, adjNode))
    return res
    
def adjListCreator(edges, n):
    adjList = {i:[] for i in range(n)}
    for weight, start, end in edges:
        adjList[start].append([end, weight])
    return adjList
    
if __name__ == "__main__":
    n = 3
    edges = [[5,0,1],[1,0,2],[3,1,2],[5,1,0],[1,2,0],[3,2,1]]
    adjList = adjListCreator(edges, n)
    print(adjList)
    print(prims(adjList, n))
