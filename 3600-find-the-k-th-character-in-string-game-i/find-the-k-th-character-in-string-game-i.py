class Solution(object):
    def kthCharacter(self, k):
        word = 'a'
        original = k
        while k > 0:
            for i in word:
                next_char = chr(ord(i)+1)
                word+=next_char
                k-=1
        
        return word[original-1]
    


        