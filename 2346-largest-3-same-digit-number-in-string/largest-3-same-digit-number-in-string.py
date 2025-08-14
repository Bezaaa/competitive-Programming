class Solution(object):
    def largestGoodInteger(self, num):
        if len(num) < 3:
            return ""
        max_num = -float("inf")
    
    
        for i in range(2 , len(num)):
            if num[i] == num[i-1] == num[i-2]:
               
                max_num = max(max_num , int(num[i-2 : i+1]))
        if max_num == 0: return "000" 
       
        return str(max_num) if max_num !=-float("inf") else ""

        