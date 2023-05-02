def rottenOranges(grid):
    m=len(grid)
    n=len(grid[0])
    que=[]
    for i in range(m):
        for j in range(n):
            if grid[i][j]==2:
                que.append((i,j))
    que.append(None)
    time=0
    while len(que)>1:
        popped_ele = que.pop(0)
        if popped_ele== None:
            time+=1
            que.append(None)
            continue
        i=popped_ele[0]
        j=popped_ele[1]
        if (0 <= i+1 < m) and (grid[i+1][j]==1):
            que.append((i+1,j))
            grid[i+1][j]=2
        if (0 <= i-1 < m) and (grid[i-1][j]==1):
            que.append((i-1,j))
            grid[i-1][j]=2
        if (0 <= j+1 < n) and (grid[i][j+1]==1):
            que.append((i,j+1))
            grid[i][j+1]=2
        if (0 <= j-1 < n) and (grid[i][j-1]==1):
            que.append((i,j-1))
            grid[i][j-1]=2
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                return -1 
    return time

if __name__ == "__main__":
    matrix = [[2,1,2],[2,1,2],[2,2,2]]
    print(rottenOranges(matrix))
