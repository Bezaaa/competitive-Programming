class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hash_map = {}
        res = []
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in hash_map:
                hash_map[sorted_nums[i]] = i
        for i in nums:
            res.append(hash_map[i])
        return res
        
        