class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_count = 0
        total = 0
        
        for row in bank:
            count = row.count('1')
            if count > 0:
                total += prev_count * count
                prev_count = count
                
        return total
        