class Solution(object):
    def maxSubsequence(self, nums, k):
        
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
     
        top_k = heapq.nlargest(k, indexed_nums, key=lambda x: x[0])
       
        top_k.sort(key=lambda x: x[1])
        
     
        return [num for num, i in top_k]
       
       