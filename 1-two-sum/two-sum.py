class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in unique:
                return [i , unique.index(complement)]
            else:
                unique.append(nums[i])
        return []

            
   
        