class Solution(object):
    def successfulPairs(self, spells, potions, success):
        
       
        potions.sort()
        ans = []

        for spell in spells:
            min_required = (success + spell - 1) // spell
            
            idx = bisect_left(potions, min_required)
            count = len(potions) - idx
            ans.append(count if count > 0 else 0)
        
        return ans

        