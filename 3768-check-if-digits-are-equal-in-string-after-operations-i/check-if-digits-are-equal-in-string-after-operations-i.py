class Solution:
    def hasSameDigits(self, s: str) -> bool:
        new_num = s

        while len(new_num) > 2:
            temp = ""
            for i in range(1, len(new_num)):
                current_sum = (int(new_num[i]) + int(new_num[i - 1])) % 10
                temp += str(current_sum)
            new_num = temp
        return new_num[0] == new_num[-1]
        
     



        