class Solution(object):
    def numIslands(self, grid):
        """
        Problem Idea:

        - For every cell in the grid, we want to count how many **islands** exist.
        - An island is a group of connected land cells (`1`) connected **vertically or horizontally**.
        - Each island should be counted **once**, even if it has many connected cells.
        - Water cells (`0`) or edges naturally bound islands.

        Approach (DFS version):

        1. Create a directions array for neighbors: up, down, left, right.
        2. Iterate through each cell in the grid:
            - If the cell is land (`1`), it is the start of a new island.
            - Increment the island count by 1.
            - Use DFS to **mark all connected land cells as visited** (convert to `0`) so they aren’t counted again.
        3. DFS helper:
            - For a given cell, check its neighbors in all directions.
            - If a neighbor is within bounds and is land (`1`), recursively visit it.
            - This ensures all cells of the current island are marked visited.
        4. Continue iterating until all cells are processed.
        5. Return the total island count.
        """

    
    
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        totalCount = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            # Mark as visited
            grid[r][c] = '0'
            # Visit neighbors
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    totalCount += 1
                    dfs(r, c)

        return totalCount
        
        