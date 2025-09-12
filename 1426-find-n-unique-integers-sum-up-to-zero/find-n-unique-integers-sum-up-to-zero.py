class Solution(object):
    def sumZero(self, n):
        """ 
        for all nums to sum up to 0
        the left sum should equal to right 0

        left_sum = -right_sum
        left_sum + right_sum = 0
        mid = n//2
        sum 
        """
        i = 0
        
        j = n -1
        res = [0]*n
        original = n
        while i < j:
            res[i] = -original
            res[j] = original
            original-=1
            i+=1
            j-=1
        return res
        

        