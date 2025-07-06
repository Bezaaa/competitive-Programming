class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = {}
      
        for num in nums2:
            self.freq[num] = self.freq.get(num, 0) + 1

        

    def add(self, index, val):
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val
        
    
        self.freq[old_val] -= 1
        if self.freq[old_val] == 0:
            del self.freq[old_val]  
        self.freq[new_val] = self.freq.get(new_val, 0) + 1
        return self.nums2  

    def count(self, tot):
        total = 0
        for num in self.nums1:
            complement = tot - num
            total += self.freq.get(complement, 0)
        return total


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)