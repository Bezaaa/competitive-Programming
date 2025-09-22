class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        max_freq = max(freq.values())
        elements = [count for num,count in freq.items() if count == max_freq]
        return sum(elements)