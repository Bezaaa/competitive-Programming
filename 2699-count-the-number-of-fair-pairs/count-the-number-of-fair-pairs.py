class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            low_target = lower - nums[i]
            high_target = upper - nums[i]

            left_index = bisect.bisect_left(nums, low_target, i + 1)
            right_index = bisect.bisect_right(nums, high_target, i + 1)

            count += (right_index - left_index)

        return count

           

          