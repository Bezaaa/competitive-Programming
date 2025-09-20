class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        
        i, j = 0, len(height) - 1
        max_left, max_right = height[i], height[j]
        total = 0
        
        while i < j:
            if max_left <= max_right:
                i += 1
                max_left = max(max_left, height[i])
                total += max_left - height[i]
            else:
                j -= 1
                max_right = max(max_right, height[j])
                total += max_right - height[j]
        
        return total 

          
        