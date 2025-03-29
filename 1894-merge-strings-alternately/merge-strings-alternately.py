class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged_string = ''
        i,j = 0,0
        while i < len (word1) and j < len(word2):
            merged_string+=word1[i]
            merged_string+=word2[j]
            i+=1
            j+=1
       
        while i < len(word1):
                merged_string+=word1[i]
                i+=1
       
        while j < len(word2):
                merged_string+=word2[j]
                j+=1
        return merged_string

        