def dfs(startRow, startCol):
    if startRow<0 or
       startCol<0 or
       startRow>=len(matrix) or
       startCol>=len(matrix[0]) or
       matrix[startRow][startCol]==newColor or
       matrix[startRow][startCol]!=initialColor:
        return None
        
    matrix[startRow][startCol] = newColor
    dfs(startRow+1, startCol)
    dfs(startRow-1, startCol)
    dfs(startRow, startCol+1)
    dfs(startRow, startCol-1)

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,0,1]]
    startRow = 1
    startCol = 0
    initialColor = matrix[startRow][startCol]
    newColor = 2
    dfs(startRow, startCol)
    for i in matrix:
        print(*i)
