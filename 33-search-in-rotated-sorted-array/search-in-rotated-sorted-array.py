class Solution(object):
    def search(self, nums, target):
        left  = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # check which side is sorted
            if nums[left] <= nums[mid]:
                # target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1  # only return -1 after the loop ends
