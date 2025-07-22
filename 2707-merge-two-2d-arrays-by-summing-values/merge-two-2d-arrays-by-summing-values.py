class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        hash_map = defaultdict(int)

       
        for id1, val1 in nums1:
            hash_map[id1] += val1

       
        for id2, val2 in nums2:
            hash_map[id2] += val2

       
        result = [[id, val] for id, val in hash_map.items()]
        result.sort(key=lambda x: x[0])

        return result
