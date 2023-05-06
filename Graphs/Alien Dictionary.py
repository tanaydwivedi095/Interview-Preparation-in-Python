from collections import defaultdict

def addEdge(adj, u, v):
	adj[ord(u) - 97].append(ord(v) - 97)

def topologicalSortUtil(adj, u, visited, st):
	visited[u] = True
	for v in adj[u]:
		if not visited[v]:
			topologicalSortUtil(adj, v, visited, st)
	st.append(u)

def topologicalSort(adj, V):
	visited = [False] * V
	st = []
	for i in range(V):
		if not visited[i]:
			topologicalSortUtil(adj, i, visited, st)
	while st:
		print(chr(st.pop() + 97), end=' ')

def printOrder(words, n, k):
	adj = defaultdict(list)
	for i in range(n - 1):
		word1 = words[i]
		word2 = words[i + 1]
		
		j = 0
		while j < len(word1) and j < len(word2):
			if word1[j] != word2[j]:
				addEdge(adj, word1[j], word2[j])
				break
			j += 1
	topologicalSort(adj, k)

if __name__ == '__main__':
	words = ["baa", "abcd", "abca", "cab", "cad"]
	n = len(words)
	k = 4
	printOrder(words, n, k)
