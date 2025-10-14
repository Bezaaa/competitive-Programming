class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        """
        Use a sliding window to check two consecutive subarrays of size k.
        For each position, check if both subarrays are strictly increasing.
        """
        def isIncreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True

        for i in range(len(nums) - 2 * k + 1):
            subArr1 = nums[i : i + k]
            subArr2 = nums[i + k : i + 2 * k]

            print(subArr1, subArr2)

            if isIncreasing(subArr1) and isIncreasing(subArr2):
                return True

        return False
