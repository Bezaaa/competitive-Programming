class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str_joined = ''.join(map(str, digits))
        num = int(str_joined) + 1

        arr = []
        while num > 0:
            digit = num % 10
            num = num // 10 
            arr.append(digit)
        return arr[::-1]