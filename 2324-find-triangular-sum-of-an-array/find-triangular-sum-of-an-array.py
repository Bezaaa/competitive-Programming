class Solution(object):
    def triangularSum(self, nums):
        
        while len(nums) > 1:
            temp = []
            for i in range(len(nums) - 1):
                temp.append((nums[i] + nums[i + 1]) % 10) 
            nums = temp
        return nums[0]
