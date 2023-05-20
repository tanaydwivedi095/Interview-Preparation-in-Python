def flyodWarshall(matrix):
    n = len(matrix)
    for i in range(0,n):
        for j in range(0,n):
            if matrix[i][j]==-1:
                matrix[i][j] = int(1e9)
            if i==j:
                matrix[i][j] = 0

    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

    for i in range(0,n):
        for j in range(0,n):
            if matrix[i][j]==int(1e9):
                matrix[i][j] = -1

    return matrix

if __name__ == "__main__":
    matrix = [[0,1,43],[1,0,6],[-1,-1,0]]
    matrix = flyodWarshall(matrix)
    for i in matrix:
        print(*i)
