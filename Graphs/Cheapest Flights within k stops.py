from math import inf

def cheapestFlight(source, dest, k, adjList):
    n =len(adjList)
    distance = [inf for i in range(0,n)]
    distance[source] = 0
    queue = []
    #node = (stops, source, weight)
    queue.append((0,source,0))
    while queue:
        stops, node, dist = queue.pop(0)
        if stops>k:
            continue
        for neighbour in adjList[node]:
            adjNode = neighbour[0]
            edW = neighbour[1]
            if dist+edW < distance[adjNode] and stops <= k:
                distance[adjNode] = dist + edW
                queue.append((stops+1, adjNode, distance[adjNode]))
    if distance[dest] == inf:
        return -1
    return distance[dest]    
    
if __name__ == "__main__":
    adjList = {
        0:[[1,5],[3,2]],
        1:[[2,5],[4,1]],
        2:[],
        3:[[1,2]],
        4:[[2,1]]
    }
    print(cheapestFlight(0,2,3,adjList))
