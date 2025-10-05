class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                x , y = matrix[row][0] , matrix[row][-1]
                if x > target or y < target:
                    continue
                else:
                    left = 0
                  
                    right = cols - 1

                    while left <= right:
                        mid = left + (right - left)//2
                        if matrix[row][mid] == target:
                            return True
                        elif matrix[row][mid] < target:
                            left = mid +1
                        else:
                            right = mid -1
        return False
        