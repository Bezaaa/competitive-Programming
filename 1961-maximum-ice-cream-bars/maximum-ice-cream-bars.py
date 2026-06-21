class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        max_icecream = 0
        curr_sum = 0
        for i in range(len(costs)):
           
            curr_sum +=costs[i]
            if curr_sum >coins:
                break
            else:
                max_icecream+=1
        return max_icecream
        
            
     
            
    
        