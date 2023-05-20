from math import inf

def bellmanFord(edges, n, start):
    distance = [inf for i in range(0,n)]
    distance[start]=0
    for i in range(0,n-1):
        for it in edges:
            u,v,wt = it
            if distance[u]!=inf and distance[u]+wt<distance[v]:
                distance[v] = distance[u]+wt
    #nth relaxation to check for negative cycles
    for it in edges:
            u,v,wt = it
            if distance[u]!=inf and distance[u]+wt<distance[v]:
                return -1
    return distance

if __name__ == "__main__":
#     node = [start, end, cost]
    edges = [[3,2,6],[5,3,1],[0,1,5],[1,5,-3],[1,2,-2],[3,4,-2],[2,4,3]]
    n=6
    start=0
    print(*bellmanFord(edges,n,start))
