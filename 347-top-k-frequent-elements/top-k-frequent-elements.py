import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """  
        Approach : heapify the nums and while k is not zero pop the elements and add
        it to the new arr return the arr when k == 0
        """
        hash_map = {}
        res = []
        for i in nums:
            hash_map[i] = hash_map.get(i , 0) + 1
        min_heap = []
        for key, val in hash_map.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        for freq , num in min_heap:
            res.append(num)
        return res

        
        

       
