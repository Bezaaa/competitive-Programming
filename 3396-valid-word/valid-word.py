class Solution(object):
    def isValid(self, word):
      
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
        
      
        if len(word) < 3:
            return False
            
        
        if not word.isalnum():
            return False
            
       
        has_vowel = any(c in vowels for c in word)
        if not has_vowel:
            return False
            
     
        has_consonant = any(c in consonants for c in word)
        if not has_consonant:
            return False
            
        return True