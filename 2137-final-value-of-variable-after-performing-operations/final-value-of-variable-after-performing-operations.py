class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        total_amount = 0 
        for i in operations:
            if i == '++X' or i=="X++":
                total_amount+=1
            else:
                total_amount-=1
        return total_amount

        