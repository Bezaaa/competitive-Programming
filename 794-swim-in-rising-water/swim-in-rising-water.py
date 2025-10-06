class Solution(object):
    def swimInWater(self, grid):
        """ 
        for each cell compare the cell next to it and the cell below it and go with the cell which has less than or equal to the current time
        to avoid repetion save or store the visited cells 
        """
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)] 
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return time  
            
            if visited[r][c]:
                continue
            visited[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    next_time = max(time, grid[nr][nc])
                    heapq.heappush(min_heap, (next_time, nr, nc))







        
        