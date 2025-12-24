class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """approach is keep monotonic stack push the small elements in the stack 
        and when the greater element happens pop them and put them in hashmap then continue this and 
        finally loop through the first arrat and if it is in the hash_map append the value of it in hasmap in  the res array
        """
        res = []
        stack = []
        hash_map = {}
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                hash_map[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for i in nums1:
            if i in hash_map:
                res.append(hash_map[i])
            else:
                res.append(-1)
        return res
       
                    
       

        