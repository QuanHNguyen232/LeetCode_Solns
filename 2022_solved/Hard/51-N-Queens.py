class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def wouldBeValid(board, row, col):
            for r in range(n):
                for c in range(n):
                    if board[r][c] == 'Q' and (r == row or c == col or abs(c - col) == abs(r - row)):
                        return False
            return True
        
        def search(board: List[str], nextRow: int):
            if nextRow == n:    # accept
                results.append(copy.copy(board))
                return
            for c in range(n):
                if wouldBeValid(board, nextRow, c): # reject
                    board[nextRow] = '.' * c + 'Q' + '.' * (n-1-c)
                    search(board, nextRow + 1)
                    board[nextRow] = '.' * n    # backtrack
        
        
        results = []
        emptyBoard = ['.' * n for i in range(n)]
        search(emptyBoard, 0)
        return results

# CodePath Week10 Session1 Lecture sln
# backtracking