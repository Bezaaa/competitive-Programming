class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1 
        def isPalindrome(left , right):
            return s[left:right+1] == s[left : right + 1][::-1]
        while left< right:
            if s[left] != s[right]:
                return isPalindrome(left+1 , right) or isPalindrome(left , right-1)
            left+=1
            right-=1
        return True
        