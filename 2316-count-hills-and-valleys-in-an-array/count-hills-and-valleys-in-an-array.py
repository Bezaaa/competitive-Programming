class Solution(object):
    def countHillValley(self, nums):
        cleaned = []
        for num in nums:
            if not cleaned or num != cleaned[-1]:
                cleaned.append(num)
        
        count = 0
      
        for i in range(1, len(cleaned) - 1):
            if (cleaned[i] > cleaned[i-1] and cleaned[i] > cleaned[i+1]) or \
            (cleaned[i] < cleaned[i-1] and cleaned[i] < cleaned[i+1]):
                count += 1
        return count

      