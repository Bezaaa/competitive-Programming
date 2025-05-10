class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count_even_digits = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count_even_digits+=1
        return count_even_digits