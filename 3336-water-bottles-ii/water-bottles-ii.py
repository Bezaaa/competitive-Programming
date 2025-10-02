class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        full = numBottles
        empty = 0
        total = 0
        
        while full > 0:
            # Drink all full bottles
            total += full
            empty += full
            full = 0
            
            # Try exchange if possible
            if empty >= numExchange:
                empty -= numExchange
                full += 1
                numExchange += 1
                
        return total
        
        