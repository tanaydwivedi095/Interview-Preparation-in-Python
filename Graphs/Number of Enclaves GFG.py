def bfs(sr,sc):
    queue = [(sr,sc)]
    delrows = [0,1,0,-1]
    delcols = [1,0,-1,0]
    while queue:
        currNode = queue.pop(0)
        row, col = currNode
        matrix[row][col] = 0
        visited[row][col] = 1
        for i in range(0,4):
            nrow = row + delrows[i]
            ncol = col + delcols[i]
            if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols and visited[nrow][ncol]==0 and matrix[nrow][ncol]==1:
                queue.append((nrow, ncol))    
        
if __name__ == "__main__":
    matrix = [[0,0,0,1],
              [0,1,1,0],
              [0,1,1,0],
              [0,0,0,1],
              [0,1,1,0]]
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[0 for col in range(0,cols)] for row in range(0,rows)]
    for row in range(0,rows):
        for col in range(0,cols):
            if (row==0 or col==0 or row==rows-1 or col==cols-1) and (matrix[row][col]==1):
                bfs(row, col)
    visited = [[0 for col in range(0,cols)] for row in range(0,rows)]
    enclaves = 0
    for row in range(0,rows):
        for col in range(0,cols):
            if matrix[row][col] == 1:
                enclaves += 1
                bfs(row,col)
    print(enclaves)
            
    
