class Solution(object):
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count_nums = 0

        for row in range(rows):
            left = 0
            right = cols - 1
            first_negative = cols 

            while left <= right:
                mid = left + (right - left) // 2

                if grid[row][mid] < 0:
                    first_negative = mid
                    right = mid - 1
                else:
                    left = mid + 1

            count_nums += cols - first_negative

        return count_nums
