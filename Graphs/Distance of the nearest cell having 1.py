def bfs(matrix, distance):
    queue = []
    visited = set()
    n = len(matrix)
    for i in range(0,n):
        for j in range(0,n):
            if matrix[i][j] == 1:
                queue.append((i,j,0))
                visited.add((i,j))
    delrow = [-1,0,1,0]
    delcol = [0,1,0,-1]
    while queue:
        currNode = queue.pop(0)
        row, col, dist = currNode
        distance[row][col] = dist
        for i in range(0,4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<n and ((nrow,ncol) not in visited):
                visited.add((nrow,ncol))
                queue.append((nrow, ncol, dist+1))
    return distance
    
if __name__ == "__main__":
    matrix = [[1,0,0],[0,1,0],[1,0,0]]
    distance = [[0 for i in range(0,len(matrix))] for j in range(0,len(matrix))]
    print(bfs(matrix, distance))
