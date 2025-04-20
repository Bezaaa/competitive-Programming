class Solution:
    def maxSum(self, nums: List[int]) -> int:
        hash_map = {}
        max_sum = -1
        for num in nums:
            max_num = max(str(num))
            if max_num in hash_map:
                hash_map[max_num].append(num)
            else:
                hash_map[max_num] = [num]
        for val in hash_map.values():
            if len(val) == 1:
                continue
            else:
                val.sort()
                max_pair_sum = val[-1] + val[-2]
                max_sum = max(max_pair_sum , max_sum)

        return max_sum
        
            
        