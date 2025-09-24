class Solution(object):
    def minWindow(self, s, t):


        if not s or not t:
            return ""
        
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        
       
        for char in t:
            hash_t[char] += 1
        
        i = 0
        min_len = float('inf') 
        min_idx = [0, 0]
        
        for j in range(len(s)):
            if s[j] in hash_t:
                hash_s[s[j]] += 1
            
           
            while all(hash_s[c] >= hash_t[c] for c in hash_t):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    min_idx = [i, j]
               
                if s[i] in hash_s:
                    hash_s[s[i]] -= 1
                i += 1
        
        return "" if min_len == float('inf') else s[min_idx[0]:min_idx[1]+1]
            


        

        