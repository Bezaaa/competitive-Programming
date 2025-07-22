class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = curr_max = nums[0]
        min_sum = curr_min = nums[0]

        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)

        return max(abs(max_sum), abs(min_sum))
      

        