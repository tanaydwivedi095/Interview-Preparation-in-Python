def depthFirstSearch(adjList, start):
    stack = [start]
    visited = set()
    visited.add(start)
    res = []
    while stack:
        currNode = stack.pop(-1)
        for neighbour in adjList[currNode]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
        res.append(currNode)
    return res

if __name__ == "__main__":
    adjList = {
        1:[2,3,4],
        2:[1,3,4],
        3:[1,2,4],
        4:[1,2,3]
    }
    start = 1
    print(depthFirstSearch(adjList, start))
