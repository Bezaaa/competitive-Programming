class Solution(object):
    def maxFreqSum(self, s):
        vowels = ['a','e','i','o','u']
        hash_v = {}
        for i in s:
            hash_v[i] = hash_v.get(i,0) + 1
      
        sorted_hash = sorted(hash_v.items(), key=lambda x: x[1])
        
        max_vowel = 0
        max_con = 0
        for i in sorted_hash:
            key , val = i
            if key in vowels:
                
                max_vowel = max(val , max_vowel)
                
            else:
               
                max_con = max(max_con , val)
        return max_vowel + max_con
                
             



        

        