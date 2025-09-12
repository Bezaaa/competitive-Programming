class Solution(object):
    def doesAliceWin(self, s):
        """
        alice starts first 
        Alice has to remove any non empty substring with odd number of vowels
        Bob has to rempve any non empty substring with even number of vowels
        The fisrt player who can't make a move on their turn loses the game
        Return True if Alice wins elsse False

        leetcoder
        for alice to move optimally she can take the longest substring wth odd number of vowels
        we start with how many vowels are present in the whole string if even we'll find the last vowel index from the last 
        when will alice lose or Draw 
         
        only if there is no vowel
        """
        vowels = ['a','e','i','o','u']
        count_vowels = 0
        for i in s:
            if i.lower() in vowels:
                count_vowels+=1
        print(count_vowels)
        if  count_vowels == 0:
            return False
        return True
     
        