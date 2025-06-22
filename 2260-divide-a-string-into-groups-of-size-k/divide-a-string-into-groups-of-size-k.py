class Solution(object):
    def divideString(self, s, k, fill):
        
        while len(s) % k != 0:
         s += fill
        res = []
        for i in range(0, len(s), k):
            res.append(s[i:i + k])
        return res