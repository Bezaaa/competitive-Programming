class Solution(object):
    def maximumLength(self, nums):
        """
       Initialize:
  count_even = number of even elements in nums
  count_odd = number of odd elements in nums
  max_alt_end_even = 0  # max length of alternating subsequence ending with even
  max_alt_end_odd = 0   # max length of alternating subsequence ending with odd

For each number in nums:
  If number is even:
    max_alt_end_even = max(max_alt_end_even, max_alt_end_odd + 1)
  Else:
    max_alt_end_odd = max(max_alt_end_odd, max_alt_end_even + 1)

Return the maximum value among:
  count_even, count_odd, max_alt_end_even, max_alt_end_odd
.
        """
         
        count_even = sum(1 for num in nums if num % 2 == 0)
        count_odd = sum(1 for num in nums if num % 2 == 1)


        max_alt_end_even = 0
        max_alt_end_odd = 0

        for num in nums:
            if num % 2 == 0:
            
                max_alt_end_even = max(max_alt_end_even, max_alt_end_odd + 1)
            else:
            
                max_alt_end_odd = max(max_alt_end_odd, max_alt_end_even + 1)

    
        return max(count_even, count_odd, max_alt_end_even, max_alt_end_odd)
