class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles 
        emptyBottles = numBottles
        while emptyBottles >=numExchange :
            fullBottles = emptyBottles // numExchange
            total += fullBottles
            emptyBottles = emptyBottles % numExchange + fullBottles

        return total
            


        
        