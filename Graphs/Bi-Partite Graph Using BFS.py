def bfs(n, adjList):
    queue = [0]
    color = [-1 for i in range(0,n)]
    while queue:
        currNode = queue.pop(0)
        for neighbour in adjList[currNode]:
            if color[neighbour] == -1:
                color[neighbour] = int(not(color[currNode]))
                queue.append(neighbour)
            elif color[neighbour] == color[currNode]:
                return False
    return True

if __name__ == "__main__":
    adjList = {
        0:[1],
        1:[2],
        2:[3],
        3:[]
    }
    print(bfs(4, adjList))
