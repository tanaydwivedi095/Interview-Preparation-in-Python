from math import inf
from heapq import heappop, heappush

class disjointset:
    def __init__(self, n):
        self.rank = [0 for i in range(0,n+1)]
        self.parent = [i for i in range(0,n+1)]

    def findUltimateParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u,v):
        ulp_u = self.findUltimateParent(u)
        ulp_v = self.findUltimateParent(v)
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_v] += 1
            
def kruskal(adjList, n):
    ds = disjointset(n)
    edges = []
    for i in range(0,n):
        for it in adjList[i]:
            end = it[0]
            weight = it[1]
            start = i
            edges.append([weight, start, end])
    edges = sorted(edges, key=lambda x:x[0])
    res = 0
    for it in edges:
        wt, start, end = it
        if ds.findUltimateParent(start) != ds.findUltimateParent(end):
            res += wt
            ds.unionByRank(start, end)
    return wt
            
def adjListCreator(edges, n):
    adjList = {i:[] for i in range(n)}
    for weight, start, end in edges:
        adjList[start].append([end, weight])
        adjList[end].append([start, weight])
    return adjList
    
if __name__ == "__main__":
    n = 3
    edges = [[5,0,1],[1,0,2],[3,1,2],[5,1,0],[1,2,0],[3,2,1]]
    adjList = adjListCreator(edges, n)
    print(kruskal(adjList, n))
