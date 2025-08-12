class Solution(object):
    def runningSum(self, nums):
        prefix_sum = [nums[0]]
        for i in nums[1:]:
            prefix_sum.append(i+ prefix_sum[-1])
        return prefix_sum
       
        