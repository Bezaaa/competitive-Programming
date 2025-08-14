class Solution(object):
    def largestGoodInteger(self, num):
        max_str = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                substring = num[i:i+3]
                if substring > max_str:
                    max_str = substring
        return max_str


        