class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_pos = 0
        count_neg = 0
        for i in nums:
            if i < 0:
                count_neg+=1
            elif i > 0:
                count_pos+=1
        return max(count_neg, count_pos)