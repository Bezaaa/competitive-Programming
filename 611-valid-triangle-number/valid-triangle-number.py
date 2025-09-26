class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        n = len(nums)
        count_valid = 0

        for k in range(n - 1, 1, -1):  
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                 
                    count_valid += (j - i)
                    j -= 1
                else:
                    i += 1

        return count_valid

        
        