class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i , j , max_len = 0 , 0 , 0
        char_set = set()
        while j < len(s):
       
            if s[j] in char_set:
                char_set.remove(s[i])
                i+=1
            else:
                char_set.add(s[j])
                j+=1
                max_len = max(max_len , j - i )
            
        return max_len
        