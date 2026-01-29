class Solution:
    def trap(self, height: List[int]) -> int:
        total_count = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
               
                floor = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                
                water_height = min(height[i], height[left]) - height[floor]
                wid = i - left -1
                total_count += wid * water_height
            stack.append(i)
        return total_count

        