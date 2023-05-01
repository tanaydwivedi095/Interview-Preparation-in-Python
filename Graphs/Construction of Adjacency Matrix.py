def constructor(edges, n):
    matrix = [[0]*(n+1) for i in range(0,n+1)]
    for edge in edges:
        start, end = edge
        matrix[start][end] = 1
        matrix[end][start] = 1
    return matrix
    
if __name__ == "__main__":
    n = 5
    edges = [[1,2],[3,5],[2,4]]
    matrix = constructor(edges,n)
    for i in matrix:
        print(*i)
