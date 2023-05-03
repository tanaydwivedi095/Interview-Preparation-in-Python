def bfs(sr, sc, baseRow, baseCol):
    pattern = f"{sr-baseRow}{sc-baseCol}"
    visited[sr][sc] = 1
    queue = [(sr,sc)]
    delRow = [1,0,-1,0]
    delCol = [0,1,0,-1]
    while queue:
        currNode = queue.pop(0)
        row, col = currNode
        for i in range(0,4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]
            if nrow>=0 and nrow<len(matrix) and ncol>=0 and ncol<len(matrix[0]) and visited[nrow][ncol]==0 and matrix[nrow][ncol]==1:
                queue.append((nrow, ncol))
                visited[nrow][ncol] = 1
                pattern += str(nrow-baseRow) + str(ncol-baseCol)
    return pattern
    
if __name__ == "__main__":
    matrix = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,1,1],[1,1,0,1,0]]
    visited = [[0 for col in range(0,len(matrix[0]))] for row in range(0,len(matrix))]
    result = set()
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == 1 and visited[i][j]==0:
                result.add(bfs(i,j,i,j))
    print(result)
    print(f"The number of distinct Islands is {len(result)}")
