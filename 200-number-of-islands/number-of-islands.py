class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        total_islands = 0
        if not grid:
            return total_islands
        

        def dfs (r , c):
            # first mark the cell and neightbours as visited 
            if (r < 0) or (r >= len(grid)) or (c < 0) or (c >= len(grid[0])) or (grid[r][c] == '0'):
                return

            # 2. MARK VISITED: Sink the ship.
            grid[r][c] = '0'

            # 3. RECURSE: Call myself on neighbors
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) #
        for r in range(len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c] == '1':
                    total_islands+=1
                dfs(r,c)
        return total_islands

        