class Solution:
    def countLargestGroup(self, n: int) -> int:
        

        def digitsSum(num: int) -> int:
            return sum(int(d) for d in str(num))

        count_groups = defaultdict(int)

        for i in range(1, n + 1):
            digit_sum = digitsSum(i)
            count_groups[digit_sum] += 1

        max_size = max(count_groups.values())
        largest_group_count = sum(1 for size in count_groups.values() if size == max_size)

        return largest_group_count
