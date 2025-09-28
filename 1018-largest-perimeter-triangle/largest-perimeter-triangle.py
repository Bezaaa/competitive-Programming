class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        
      
       
        max_perimeter = 0
        for i in range(len(nums)-2):
            if nums[i] + nums[i +1] > nums[i+2]:
                curr_per = nums[i] + nums[i+1] + nums[i+2]
                max_perimeter = max(max_perimeter , curr_per)
                
        return max_perimeter
            


        
        