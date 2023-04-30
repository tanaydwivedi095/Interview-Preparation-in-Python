def solveNQueens(n):
    ans = []
    board = ["."*n for j in range(0,n)]
    solve(0, board, ans, n)
    return ans

def solve(col, board, ans, n):
    if col==n:
        print(board)
    for row in range(0,n):
        if isSafe(row, col, board, n):
            board[row][col] = "Q"
            solve(col+1, board, ans, n)
            board[row][col] = "."

def isSafe(row, col, board, n):
    duprow = row
    dupcol = col
    while row>=0 and col>=0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1
    col = dupcol
    row = duprow
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1
    col = dupcol
    row = duprow
    while row<n and col>=0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1
        
if __name__ == "__main__":
    n = 8
    print(solveNQueens(n))
