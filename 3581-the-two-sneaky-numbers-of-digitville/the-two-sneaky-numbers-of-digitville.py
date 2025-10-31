class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for num ,val  in count.items():
            if val == 2:
                res.append(num)
        return res
