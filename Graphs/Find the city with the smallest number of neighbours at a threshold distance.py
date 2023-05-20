def smallestCity(n, edges, distanceThreshold):
    matrix = [[1e9 for col in range(n)] for row in range(n)]
    for edge in edges:
        u,v, wt = edge
        matrix[u][v] = wt
        matrix[v][u] = wt
    for i in range(0,n):
        matrix[i][i] = 0
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if matrix[i][k]==1e9 or matrix[k][j]==1e9:
                    continue
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
    cntCity = n
    cityNo = -1
    for city in range(0,n):
        cnt=0
        for adjCity in range(0,n):
            if matrix[city][adjCity] <= distanceThreshold:
                cnt+=1
        if cnt<=cntCity:
            cntCity = cnt
            cityNo = city
    return cityNo

if __name__ == "__main__":
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    n = 4
    distanceThreshold = 4
    print(smallestCity(n,edges, distanceThreshold))
