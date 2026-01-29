class Solution:
    def trap(self, height: List[int]) -> int:
        """  
        Approach is when do we calculate how much water it contains
        the bottlneck is the shorter height 
        meaning we use stack and as long as the next element is shorter than the top element in the stack
        we add the index of the element to the stack
        when we encounter a taller element we calculate the size of the stack and add it to the total count
        finally return the tottal count
        
        """ 
        stack = []
        res = 0
        for i in range(len(height)):
            # 1. While current height is a "Right Wall" (taller than top of stack)
            while stack and height[i] > height[stack[-1]]:
                
                # 2. Pop the "Floor"
                mid = stack.pop()
                
                # if no left wall exists, water leaks out. Break the while loop.
                if not stack:
                    break
                    
                # Identify the "Left Wall" (the new top of the stack)
                left = stack[-1]
                
                
                # height = (shorter of two walls) - floor
                h = min(height[left], height[i]) - height[mid]
                
              
                w = i - left - 1
                
                res += h * w
                
          
            stack.append(i)
        return res
                