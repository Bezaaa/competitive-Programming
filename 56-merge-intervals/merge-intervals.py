class Solution(object):
    def merge(self, intervals):
        
        if not intervals:
            return []
        intervals.sort(key= lambda x:x[0])
        res  = [intervals[0]]
        for i in range(1,len(intervals)):
            prev = res[-1]
            current = intervals[i]
            if prev[1] >= current[0]:
                prev[1] = max(current[1], prev[1])
                
            else:
                res.append(current)
        return res


      
        
      

       
        