class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged_string = ''
        i = 0
        shortest_len = min(len(word1) , len(word2))
        while i < shortest_len : 
            merged_string +=word1[i]
            merged_string+=word2[i]
            i+=1
        if len(word1) > shortest_len:
             merged_string += word1[i:]
        if len(word2) > shortest_len:
             merged_string += word2[i:]
        return merged_string
            

        