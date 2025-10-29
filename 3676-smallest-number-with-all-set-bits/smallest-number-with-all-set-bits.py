class Solution:
    def smallestNumber(self, n: int) -> int:
        current_num = bin(n)[2:]
        new_num = ''
        
        if all(char == '1' for char in current_num):
            
            return n
        else:
            new_num = current_num.replace('0','1')
        return int(new_num , 2)


    
        