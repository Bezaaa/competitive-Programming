class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hash_map = {}
        for i in arr:
            hash_map[i] = hash_map.get(i,0) + 1
        max_num = -1
        for i in arr:
            if hash_map[i] == i:
                max_num = max(max_num , i)
        return max_num           
        