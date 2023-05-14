from math import *
from heapq import heappush, heappop, heapify

def dijkstra(start, nodes, adjList, distance):
    visited = set()
    minHeap = [[0,start]]
    distance[start] = 0
    while minHeap:
        currNode = heappop(minHeap)
        dis, node = currNode
        for neighbour in adjList[node]:
            edgeWeight = neighbour[1]
            adjNode = neighbour[0]
            if dis + edgeWeight < distance[adjNode]:
                distance[adjNode] = dis + edgeWeight
                heappush(minHeap, [distance[adjNode], adjNode])
    return {i:distance[i] for i in range(nodes)}
    
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
    startNode = 0
    distance = dijkstra(startNode, numberOfNodes, adjList, distance)
    for k,v in distance.items():
        print(f"The shortest distance of node {k} from node {startNode} is {v} units")
