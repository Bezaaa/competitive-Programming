class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken_map = {}
    
        count_words = 0

        textList = text.split()

        for i in brokenLetters:
            broken_map[i] = broken_map.get(i,0) + 1
       
        for text in textList:
            if all(c not in broken_map for c in text):
                count_words+=1
        return count_words