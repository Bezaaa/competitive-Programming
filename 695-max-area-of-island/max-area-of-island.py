class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_count  = 0
        total_count =0
        if not grid:
            return total_count
        rows = len(grid)
        cols = len(grid[0])
        def dfs (r , c):
            if r >= rows or c>=cols or r< 0 or c<0 or grid[r][c] == 0: 
                return  0
            grid[r][c] =0
                
           
           
           
            
            return 1 +  dfs(r+1 , c) +  dfs(r-1 , c) +  dfs(r , c + 1) + dfs(r , c-1)
         
        for  r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = dfs(r,c)
                    max_count = max(max_count , current_area)
                    
        return max_count

        