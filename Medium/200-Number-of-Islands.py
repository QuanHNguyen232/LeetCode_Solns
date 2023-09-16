class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # there are different approaches for this problem
        # Here I use Union-Find since it is in CodePath Summer22 Week7 Session2 lecture
        
        # convert grid to index: row*#cols + col
        # e.g: row1 col2: 1*3 + 2 = 5
        #
        # row|col:   0  1  2
        #
        #   0        0, 1, 2
        #   1        3, 4, 5
        
        nrows = len(grid)
        ncols = len(grid[0])
        parent = [i for i in range(nrows*ncols)]
        # use self to use globally
        self.num_islands = sum([grid[i][j]=='1' for i in range(nrows) for j in range(ncols)])
        
        def find(x):
            '''
            input: island index
            output: index of root of that island
            '''
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(x,y):
            '''
            input: 2 islands need to union
            output: union of 2 islands
            '''
            # get the root of each island
            xroot, yroot = find(x), find(y)
            # union if they have different roots
            if xroot != yroot:
                parent[xroot] = yroot
                # every time union, decrease num_island by 1
                self.num_islands -= 1
        
        
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == '1':
                    # convert to index
                    i = row*ncols + col
                    # check left island
                    if col > 0 and grid[row][col-1] == '1':
                        union(i, i - 1)
                    # check upper island
                    if row > 0 and grid[row-1][col] == '1':
                        union(i, i - ncols)
                    # only need to check left and upper since we go from left->right & top->bottom
                    
        return self.num_islands

# This is solution from CodePath Summer22 Week7 Session2 lecture
        
        
        