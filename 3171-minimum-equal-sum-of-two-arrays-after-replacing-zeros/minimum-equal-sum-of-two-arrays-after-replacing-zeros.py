class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # if the array of smaller sum doesn't have 0s there is no way to increase the sum so answer is -1
        # if both arrays have 0s replace them with 1 and take the maximum of the 2 sums

        min_sum = 0
        sum_1 = 0
        sum_2 = 0
       

        for  i in nums1:
            if i ==0:
                sum_1+=1
            sum_1+=i
        for j in nums2:
            if j == 0:
                sum_2+=1
            sum_2+=j
        min_sum = max(sum_1 , sum_2)
        if 0 not in nums1 and sum_1 < sum_2 or 0 not in nums2 and sum_2 < sum_1:
            return -1
        return min_sum
        