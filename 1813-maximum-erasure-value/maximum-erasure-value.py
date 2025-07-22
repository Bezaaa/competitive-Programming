class Solution(object):
    def maximumUniqueSubarray(self, nums):
        i = 0
        j = 0
        max_sum = 0
        curr_sum = 0
        hash_map = {}
        
        while j < len(nums):
            while hash_map.get(nums[j], 0) > 0:
                hash_map[nums[i]] -= 1
                curr_sum -= nums[i]
                i += 1
            
            hash_map[nums[j]] = hash_map.get(nums[j], 0) + 1
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
            j += 1
        
        return max_sum
        