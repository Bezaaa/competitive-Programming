class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, visited, prev_height):
            if (
                (r, c) in visited or
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Pacific Ocean (top row and left column)
        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])  # Left column
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])  # Right column

        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])  # Top row
            dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])  # Bottom row

        # Cells reachable by both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result
    