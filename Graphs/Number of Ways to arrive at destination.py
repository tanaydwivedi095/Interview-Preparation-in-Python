from math import inf
from heapq import heappop, heappush

def numWays(adjList, n):
    minHeap = []
    heappush(minHeap, (0,0))
    distance = [inf for i in range(n)]
    ways = [0 for i in range(n)]
    distance[0] = 0
    ways[0] = 1
    while minHeap:
        dis, node = heappop(minHeap)
        for it in adjList[node]:
            adjNode, edW = it
            if dis+edW < distance[adjNode]:
                distance[adjNode] = dis+edW
                heappush(minHeap, (distance[adjNode], adjNode))
                ways[adjNode] = ways[node]
            elif dis+edW == distance[adjNode]:
                ways[adjNode]=(ways[adjNode] + ways[node])%(10**9+7)
    return ways[n-1]%(10**9 + 7)
            
    
    
if __name__ == "__main__":
    adjList = {
        0:[[1,1],[2,2],[3,1],[4,2]],
        1:[[0,1],[5,2]],
        2:[[0,2],[5,1]],
        3:[[0,1],[5,2],[7,3],[6,2]],
        4:[[0,2],[6,1]],
        5:[[1,2],[2,1],[3,2],[8,1]],
        6:[[3,2],[4,1],[8,1]],
        7:[[3,3],[8,1]],
        8:[[5,1],[7,1],[6,1]]
    }
    print(numWays(adjList, 9))
