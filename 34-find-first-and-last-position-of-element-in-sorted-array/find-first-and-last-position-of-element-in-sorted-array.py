class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # nums[mid] == target
                # Expand to find boundaries
                start = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                end = mid
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                return [start, end]
        
        return res