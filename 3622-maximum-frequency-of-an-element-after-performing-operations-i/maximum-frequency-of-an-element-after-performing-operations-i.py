class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        max_num = max(nums)
        frequency = [0] * (max_num + 1) 
        prev_window_sum = 0
        max_freq = 0

        # Build frequency array
        for num in nums:
            frequency[num] += 1

        current_window_sum = sum(frequency[:k])  # sum of frequencies in the first k elements

        for num in range(max_num + 1):
            # Slide the window forward
            current_window_sum -= frequency[num]  # remove leftmost element of window
            if num + k <= max_num:
                current_window_sum += frequency[num + k]  # add new rightmost element of window

            # Track frequencies in the previous window
            if num > 0:
                prev_window_sum += frequency[num - 1]
            if num > k:
                prev_window_sum -= frequency[num - k - 1]

            # Maximum frequency considering current element
            max_freq = max(max_freq, frequency[num] + min(numOperations, prev_window_sum + current_window_sum))

        return max_freq
