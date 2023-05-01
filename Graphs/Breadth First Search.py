def breadthFirstSearch(start,adjList):
    queue = [start]
    visited = set()
    visited.add(start)
    res = []
    while queue:
        currNode = queue.pop(0)
        for neighbour in adjList[currNode]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
        res.append(currNode)
    return res

if __name__ == "__main__":
    adjList = {
        1:[2],
        2:[4],
        3:[4],
        4:[1,3]
    }
    start = 4
    print(breadthFirstSearch(start, adjList))
