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
    
    def numberOfProvinces(self):
        print(self.parent)
        return len(set(self.parent))

if __name__ == "__main__":
    ds = disjointset(7)
    ds.unionByRank(0,3)
    ds.unionByRank(1,2)
    ds.unionByRank(2,3)
    ds.unionByRank(4,5)
    ds.unionByRank(6,7)
    ds.unionByRank(5,6)
    ds.unionByRank(3,7)
    print(ds.numberOfProvinces())
