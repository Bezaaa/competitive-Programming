class Solution(object):
    def minScoreTriangulation(self, values):
        hash_map = {}
        score = float('inf')
        def helper(i, j):
            if j - i < 2:
                return 0
            
            if (i, j) in hash_map:
                return hash_map[(i, j)]
            
            score = float('inf')
            for k in range(i+1, j):
                triangle = values[i] * values[k] * values[j]
                total = helper(i, k) + helper(k, j) + triangle
                score = min(score, total)
            
            hash_map[(i, j)] = score
            return score
    
               
          
        return helper(0,len(values)-1)



        