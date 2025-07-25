class Solution(object):
    def maxSum(self, nums):
        unique = sorted(list(set(nums)))
        if unique[-1] < 0:
            return unique[-1]
        max_sum = 0
        for i in unique:
            if i > 0:
                max_sum+=i
        return max_sum

      
        

        
        