from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows , cols = len(grid) , len(grid[0])
        
        queue = deque()
        minutes = 0
        fresh = 0
        #  add the rotten ones in the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                # we count the fresh oranges here
                if grid[r][c] == 1:
                    fresh+=1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            minutes +=1
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr , dc in directions:
                     nr, nc = r + dr, c + dc
                    #  make the neighbours rotten
                     if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        queue.append((nr, nc))
                        fresh -= 1
        return minutes if fresh == 0 else -1
                     
            
                
            