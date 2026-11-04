class Solution:
    def isValid(self, s: str) -> bool:
       
        stack  = []
        b_map = {
            "(" : ')',
            "{" : '}',
            "[":"]"
        
        }
        if len(s) == 1:
            return False
        for char in s:
            if char in b_map: 
                stack.append(b_map[char])
            else:  
                if not stack or stack.pop() != char:
                    return False
        
        return len(stack) == 0
                

