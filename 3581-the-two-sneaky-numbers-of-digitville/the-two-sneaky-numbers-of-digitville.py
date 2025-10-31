class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = set()
        for num in nums:
            if count[num] == 2:
                res.add(num)
        return list(res)
