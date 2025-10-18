class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        last_picked = float('-inf')
        distinct_count = 0

        for num in nums:
          
            pick = max(num - k, last_picked + 1)

           
            if pick <= num + k:
                distinct_count += 1
                last_picked = pick

        return distinct_count
