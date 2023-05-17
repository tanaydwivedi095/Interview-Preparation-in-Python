from heapq import heappop, heappush, heapify
from math import inf

def shortestPath(matrix, src, dstn):
    sr, sc = src
    dr, dc = dstn
    row = len(matrix)
    col = len(matrix[0])
    dist = [[inf for c in range(0,col)] for r in range(0,row)]
    dist[sr][sc] = 0
    minHeap = []
    heappush(minHeap, (0,sr,sc))
    directions = [1,0,-1,0]
    while minHeap:
        currNode = heappop(minHeap)
        distance, r, c = currNode
        for i in range(0,4):
            nrow = r + directions[i]
            ncol = c + directions[(i+1)%4]
            if nrow>=0 and nrow<row and ncol>=0 and ncol<col and matrix[nrow][ncol]!=0:
                if distance + 1 < dist[nrow][ncol]:
                    dist[nrow][ncol] = distance+1
                    heappush(minHeap, (distance+1, nrow, ncol))
    return dist[dr][ds]
    
    
if __name__ == "__main__":
    matrix = [
        [1,1,1,1],
        [1,1,0,1],
        [1,1,1,1],
        [1,1,0,0],
        [1,0,0,0]
    ]
    source = [0,1]
    destination = [2,2]
    distance = shortestPath(matrix, source, destination)
    print(distance)
