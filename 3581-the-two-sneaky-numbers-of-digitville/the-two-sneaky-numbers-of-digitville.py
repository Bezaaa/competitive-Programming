class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        hash_map = {}
        for i in nums:
            if i in hash_map:
                res.append(i)
            hash_map[i] = 1
        return res
        