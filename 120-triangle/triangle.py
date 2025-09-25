class Solution(object):
    def minimumTotal(self, triangle):
        visited = {}  

        def dfs(i, j):
         
            if (i, j) in visited:
                return visited[(i, j)]

         
            if i == len(triangle) - 1:
                return triangle[i][j]

          
            left = dfs(i + 1, j)
            right = dfs(i + 1, j + 1)

            
            visited[(i, j)] = triangle[i][j] + min(left, right)
            return visited[(i, j)]

      
        return dfs(0, 0)

                

    


        
        