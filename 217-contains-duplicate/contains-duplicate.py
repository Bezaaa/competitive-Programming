class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique = set()
        for i in nums:
            if i in unique:
                return True
            unique.add(i)
        return False
        