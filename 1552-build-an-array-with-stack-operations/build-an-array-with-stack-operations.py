class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        target_ptr = 0
        for i in range(1 , n + 1):
            if target_ptr == len(target):
                break
            res.append("Push")
            
            if target[target_ptr] == i:
                target_ptr +=1
            else:
                res.append("Pop")
            
        return res
        
        
       

        
        
