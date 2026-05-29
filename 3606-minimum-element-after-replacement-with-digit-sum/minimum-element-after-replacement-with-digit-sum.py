class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float('inf')
        def calcSum(num):
            curr_sum = sum([int(i) for i in num])
            return curr_sum
        
            
           
        for i in nums:
            min_num = min(min_num , calcSum(str(i)))
        return min_num

        