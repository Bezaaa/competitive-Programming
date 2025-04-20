class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index < len(nums) :
            return index
        else:
            return len(nums) 
        
              


        