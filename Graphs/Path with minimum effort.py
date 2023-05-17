from math import inf
from heapq import heappush, heappop
from pandas import DataFrame

def minEffort(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    distance = [[inf for col in range(0,cols)] for row in range(0,rows)]
    #node = [diff, row, col]
    minHeap = []
    heappush(minHeap, (0,0,0))
    directions = [1,0,-1,0]
    while minHeap:
        currNode = heappop(minHeap)
        diff, row, col = currNode
        if row==rows-1 and col==cols-1:
            return diff
        for i in range(0,4):
            nrow = row + directions[i]
            ncol = col + directions[(i+1)%4]
            if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols:
                newEffort = max(abs(matrix[row][col]-matrix[nrow][ncol]), diff)
                if distance[nrow][ncol] > newEffort:
                    distance[nrow][ncol] = newEffort
                    heappush(minHeap, (newEffort, nrow, ncol))
    
if __name__ == "__main__":
    matrix = [[1,2,2],[3,8,2],[5,3,5]]
    for i in matrix:
        print(*i)
    print(minEffort(matrix))
