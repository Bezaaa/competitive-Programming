class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_diff = -1
        for i in range(len(nums)-1):
            for j in range(i+1 ,len(nums)):
                if nums[i] < nums[j] :
                    max_diff = max(nums[j]-nums[i] , max_diff)
        return max_diff


        