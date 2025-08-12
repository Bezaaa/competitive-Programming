class Solution(object):
    def pivotIndex(self, nums):
        """ 
        left  + pivot  = total - (right + pivot)
        
        """
        prefix_sum = [nums[0]]

        for i in nums[1:]:
            prefix_sum.append(i + prefix_sum[-1])
        total_sum = prefix_sum[-1]
        for i in range(len(prefix_sum)):
            left = prefix_sum[i-1] if i > 0 else 0
            if  total_sum - prefix_sum[i] == left:
               return i
        return -1
            

        

       