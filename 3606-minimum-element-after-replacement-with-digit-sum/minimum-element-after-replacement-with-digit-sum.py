class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float('inf')
        def calcSum(num):
            curr_sum = 0
            while num > 0:
                digit = num % 10
                curr_sum+=digit
                num = num // 10
            return curr_sum
        for i in nums:
            min_num = min(min_num , calcSum(i))
        return min_num

        