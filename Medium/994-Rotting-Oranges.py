class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        
        queue = deque()
        total_orange = 0
        
        for row in range(n_rows):
            for col in range(n_cols):
                # count total orange
                if grid[row][col]!=0:
                    total_orange += 1
                # add all rotten into queue
                if grid[row][col] == 2:
                    queue.append((row, col, 0)) # row, col, time
        
        if total_orange == 0: return 0
        if len(queue)==0: return -1
        
        # BFS
        curr_time = 0
        while queue:
            curr_r, curr_c, curr_time = queue.popleft()
            
            # check all surrounding oranges
            for r2, c2 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_r = curr_r + r2
                new_c = curr_c + c2
                
                # update fresh -> rotten
                if (0 <= new_r < n_rows) and (0 <= new_c < n_cols) and (grid[new_r][new_c]==1):
                    queue.append((new_r, new_c, curr_time + 1))
                    grid[new_r][new_c] = 2
                    
        # if all are rotten, total_orange == total number of orange value 2
        return curr_time if (total_orange == sum([sum(row) for row in grid]) // 2) else -1