class Solution:
    def isPalindrome(self, s: str) -> bool:
        replaced = re.sub(r'[^a-zA-Z0-9]+', '', s)
        i = 0
        j = len(replaced) - 1
        while i < j:
            if replaced[i].lower() !=replaced[j].lower():
                
                return False
            i+=1
            j-=1
        return True