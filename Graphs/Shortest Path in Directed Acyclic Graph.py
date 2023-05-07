import math

def topologicalSort(queue):
    while queue:
        currNode = queue.pop(0)
        topo.append(currNode)
        for neighbour in adjList[currNode]:
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                queue.append(neighbour)

def inDegreeCalculator(adjList):
    inDegree = {key:0 for key in adjList.keys()}
    for key, value in adjList.items():
        for element in value:
            inDegree[element] = inDegree.get(element, 0) + 1
    return inDegree
    
def adjListCreator(adjListWithWeights):
    adjList = {}
    for key, value in adjListWithWeights.items():
        if len(value)>0:
            adjList[key] = adjList.get(key, []) + [value[0][0]]
        else:
            adjList[key] = []
    return adjList

if __name__ == "__main__":
    #structure = node : [neighbour, weight]
    n = 7
    adjListWithWeights = {
        0:[[1,2]],
        1:[[3,1]],
        2:[[3,3]],
        3:[],
        4:[[0,3],[2,1]],
        5:[[4,1]],
        6:[[4,2],[5,3]]
    }
    adjList = adjListCreator(adjListWithWeights)
    inDegree = inDegreeCalculator(adjList)
    topo, queue = [], []
    for k,v in inDegree.items():
        if v==0:
            queue.append(k)
    topologicalSort(queue)
    stack = []
    for i in topo:
        stack.append(i)
    distance = [math.inf for i in range(0,n)]
    distance[0] = 0
    while stack:
        node = stack.pop(-1)
        for neighbour in adjList[node]:
            v = neighbour
            try:
                weight = adjListWithWeights[neighbour][0][1]
            except:
                weight = 0
            if distance[node] + weight < distance[v]:
                distance[v] = distance[node] + weight
    print(distance)
