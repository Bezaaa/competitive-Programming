class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0 
        nums_set = set()
        for i in nums:
            nums_set.add(i)
        for i in nums_set:
            if i - 1 not in nums_set:
                current = i
                while current in nums_set:
                    current+=1
                max_len = max(max_len  , current -i)
        return max_len