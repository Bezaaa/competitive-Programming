class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
        heights.append(0)
        
        stack = [] 
        max_area = 0
        
        for i in range(len(heights)):
            # Step 2: If we find a bar shorter than the top of our stack,
            # the bar on top has hit its "Right Boundary".
            while stack and heights[i] < heights[stack[-1]]:
                # Step 3: Pop the bar we want to calculate the area for.
                h_index = stack.pop()
                h = heights[h_index]
                
               
                if not stack:
                    width = i
                else:
                 
                    width = i - stack[-1] - 1
                
                max_area = max(max_area, h * width)
            
            stack.append(i)
            
        return max_area