def dfs(node, stack):
    visited[node] = 1
    for neighbour in adjList[node]:
        if visited[neighbour]==0:
            dfs(neighbour, stack)
    stack.append(node)
    return stack

if __name__ == "__main__":
    n = 6
    visited = [0 for i in range(0,n)]
    adjList = {0:[], 1:[], 2:[3], 3:[1], 4:[0,1], 5:[0,2]}
    stack = []
    for i in range(0,n):
        if visited[i]==0:
            stack = dfs(i, stack)
    ans = []
    while stack:
        ans.append(stack.pop(-1))
    print(ans)
