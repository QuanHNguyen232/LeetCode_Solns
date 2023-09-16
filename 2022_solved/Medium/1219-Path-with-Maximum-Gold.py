class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        def dfs(r,c):
            curr_val = grid[r][c]
            grid[r][c] = 0  # use to mark as visited
            ans = 0
            
            # check all 4 adjacent cells
            for x,y in ((r+1,c),(r-1,c),(r,c-1),(r,c+1)):
                # check in bound and has gold
                if 0 <= x < n_rows and 0 <= y < n_cols and  grid[x][y] != 0:
                    ans = max(ans, dfs(x, y))
            
            grid[r][c] = curr_val
            return ans + curr_val
        
        
        ans = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] != 0:
                    # update the max gold collected
                    ans = max(ans, dfs(i, j))
        
        return ans
