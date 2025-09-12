class Solution(object):
    def doesAliceWin(self, s):
   
  
        vowels = ['a','e','i','o','u']
        for i in s:
            if i.lower() in vowels:
                return True
        return False
        