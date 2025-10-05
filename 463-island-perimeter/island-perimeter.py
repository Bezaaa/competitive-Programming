class Solution(object):
    def islandPerimeter(self, grid):
        """
        For each land cell, check all 4 directions.
        If the neighbor is out of bounds or is water (0), 
        increment the perimeter.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                            perimeter += 1
        return perimeter
