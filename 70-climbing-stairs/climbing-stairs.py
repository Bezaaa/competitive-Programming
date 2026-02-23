class Solution(object):
   
        
   
    def climbStairs(self, n):
        one = 1
        two = 1
        for i in range(1 ,n):
            temp = one 
            one = one + two 
            two = temp 
        return one


            
        