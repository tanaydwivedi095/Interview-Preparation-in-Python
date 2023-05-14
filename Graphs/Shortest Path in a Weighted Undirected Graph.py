from math import *
from heapq import heappush, heappop, heapify

def shortestPath(source, target, adjList):
    minHeap = [(0,source)]
    parent = [i for i in range(0,len(adjList))]
    distance[source] = 0
    while minHeap:
        currNode = heappop(minHeap)
        dis, node = currNode
        for neighbour in adjList[node]:
            adjNode = neighbour[0]
            edW = neighbour[1]
            if dis+edW < distance[adjNode]:
                distance[adjNode] = dis + edW
                heappush(minHeap, (distance[adjNode], adjNode))
                parent[adjNode] = node
    
    if distance[target]== inf:
        return -1
    path = []
    node = target
    while parent[node]!=node:
        path.append(node)
        node = parent[node]
    path.append(0)
    return path[::-1]
    
def adjListCreator():
    adjList = {
        # node:[[neighbour, weight]]
        0:[[1,4],[2,4]],
        1:[[0,4],[2,2]],
        2:[[0,4],[1,2],[3,3],[4,1]],
        3:[[2,3],[5,2]],
        4:[[2,1],[5,3]],
        5:[[3,2],[4,3]]
    }
    return adjList
    
if __name__ == "__main__":
    adjList = adjListCreator()
    numberOfNodes = len(adjList.keys())
    distance = [inf for i in range(0,numberOfNodes)]
    source = 0
    target = 5
    distance = shortestPath(source, target, adjList)
    print(distance)
