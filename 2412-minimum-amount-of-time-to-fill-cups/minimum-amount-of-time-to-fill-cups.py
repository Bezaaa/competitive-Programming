

class Solution(object):
    def fillCups(self, amount):
        total_sec = 0
        # Convert to max heap by negating values
        amount = [-num for num in amount if num > 0]
        heapq.heapify(amount)

        while amount:
            # Pop the most filled cup
            top1 = -heapq.heappop(amount)

            # If there’s at least one more cup with water
            if amount:
                top2 = -heapq.heappop(amount)
            else:
                top2 = 0

            # Reduce both by 1 (simulate drinking from two different cups)
            top1 -= 1
            top2 -= 1

            # Push back if there's still water left
            if top1 > 0:
                heapq.heappush(amount, -top1)
            if top2 > 0:
                heapq.heappush(amount, -top2)

            total_sec += 1

        return total_sec
