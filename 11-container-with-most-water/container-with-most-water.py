class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i <= j :
            width = j - i
            curr_area = width * min(height[j] , height[i])
            max_area = max(max_area , curr_area)
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return max_area


        