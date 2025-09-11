class Solution(object):
    def sortVowels(self, s):
        vowels_array = []
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])  

      
        for ch in s:
            if ch in vowels:
                vowels_array.append(ch)

      
        vowels_array.sort()
        
        j = 0
        result = []  

       
        for ch in s:
            if ch in vowels:     
                result.append(vowels_array[j])
                j += 1
            else:
                result.append(ch)

        return "".join(result)
