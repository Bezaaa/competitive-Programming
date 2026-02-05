class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        total_islands = 0
        if not grid:
            return 0
        def dfs(r , c):
            
            if (r < 0) or (r >= len(grid)) or (c < 0) or (c >= len(grid[0])) or (grid[r][c] == '0'):
                return
             
            if grid[r][c] == '1':
                grid[r][c] = '0'
            dfs(r ,c+1)
            dfs(r, c-1)
            dfs(r+1 , c)
            dfs(r-1 , c)
            return grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    total_islands+=1
                    dfs(i ,j)
        return total_islands

       
        