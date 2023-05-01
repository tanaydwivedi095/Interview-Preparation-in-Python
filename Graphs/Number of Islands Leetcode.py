def traversal():
    res = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(0,rows):
        for col in range(0,cols):
            if matrix[row][col] == 1:
                res += 1
                dfs(row, col, rows, cols)
    return res

def dfs(row, col, rows, cols):
    if row<0 or col<0 or row>=rows or col>=cols or matrix[row][col]==0:
        return None
    matrix[row][col] = 0
    dfs(row+1, col, rows, cols)
    dfs(row-1, col, rows, cols)
    dfs(row, col+1, rows, cols)
    dfs(row, col-1, rows, cols)
    

if __name__ == "__main__":
    matrix = [[0,1,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,0],[1,1,0,1]]
    print(traversal())
