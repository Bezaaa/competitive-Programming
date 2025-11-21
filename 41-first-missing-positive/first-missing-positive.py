class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = len(nums)
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
       
        for i in range(len(nums)):
            if nums[i]-1!=i:
          
                return i+1
        return max_num + 1