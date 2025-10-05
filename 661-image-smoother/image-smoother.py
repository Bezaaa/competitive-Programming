class Solution(object):
    def imageSmoother(self, img):
        directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
            ]
      
        rows  = len(img)
        cols = len(img[0])
        new_matrix = [[0] * cols for _ in range(rows)]
        print(new_matrix)
        for row in range(rows):
            for col in range(cols):
                total = img[row][col]
                count = 1
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        total += img[nr][nc]
                        count += 1
                smoothed = total // count
                new_matrix[row][col] = smoothed
        return new_matrix

