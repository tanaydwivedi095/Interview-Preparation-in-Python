def constructor(edges):
    adjList = dict()
    for edge in edges:
        start, end = edge
        if start not in adjList:
            adjList[start] = [end]
        else:
            adjList[start].append(end)
    return adjList

if __name__ == "__main__":
    edges = [[1,2],[2,3],[3,4]]
    print(constructor(edges))
