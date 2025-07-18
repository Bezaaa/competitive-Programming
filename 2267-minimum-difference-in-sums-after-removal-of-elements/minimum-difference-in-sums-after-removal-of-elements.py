

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3

        # Step 1: Calculate prefix sums (left side) - minimize the first n elements' sum
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        left_sum = sum(nums[:n])
        left_sums = [left_sum]

        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(max_heap)  # remove largest
            left_sums.append(left_sum)

        # Step 2: Calculate suffix sums (right side) - maximize the second n elements' sum
        min_heap = nums[-n:]
        heapq.heapify(min_heap)
        right_sum = sum(min_heap)
        right_sums = [0] * (n + 1)
        right_sums[n] = right_sum

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i] - heapq.heappop(min_heap)  # remove smallest
            right_sums[i - n] = right_sum

        min_diff = float('inf')
        for i in range(n + 1):
            min_diff = min(min_diff, left_sums[i] - right_sums[i])

        return min_diff
