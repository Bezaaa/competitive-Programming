class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False] * len(nums)
        total_score = 0

        
        indexed_nums = sorted(enumerate(nums), key=lambda x: x[1])
        print(indexed_nums)

        for idx, value in indexed_nums:
            if not marked[idx]:
                total_score += value
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < len(nums) - 1:
                    marked[idx + 1] = True

        return total_score

            



        