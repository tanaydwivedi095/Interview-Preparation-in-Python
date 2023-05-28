class disjointset:
    def constructor(self, n):
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
            
class Solution(disjointset):
    def Solve(self, n, adj):
        self.constructor(n)
        cntExtra = 0
        for start, end in adj:
            if self.findUltimateParent(start) == self.findUltimateParent(end): cntExtra += 1
            else: self.unionByRank(start, end)
        cntC = 0
        for i in range(0,n):
            if self.parent[i] == i: cntC+= 1
        ans = cntC-1
        if cntExtra>=ans: return ans
        return -1
    
if __name__ == "__main__":
    n = 4
    adj = [ [0, 1] , [0, 2] , [1, 2] ]
    sol = Solution()
    print(sol.Solve(n, adj))
