class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count_symmetric = 0
        
        def isSymmetric(num: str) -> bool:
            n = len(num)
            if n % 2 != 0:
                return False
            mid = n // 2
            first_sum = sum(int(d) for d in num[:mid])
            second_sum = sum(int(d) for d in num[mid:])
            return first_sum == second_sum
        
        for i in range(low , high + 1):
            if isSymmetric(str(i)):
                count_symmetric+=1
        return count_symmetric

        