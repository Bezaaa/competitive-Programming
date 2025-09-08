class Solution(object):
    def getNoZeroIntegers(self, n):
        def has_zero(x):
         return '0' in str(x)
    
        for i in range(1, n):
            diff = n - i
            if not has_zero(i) and not has_zero(diff):
                return [diff, i]
        