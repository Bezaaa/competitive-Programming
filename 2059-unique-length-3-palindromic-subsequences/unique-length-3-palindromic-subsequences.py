class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0  # Count of unique (X, Y, X) triplets
        
        for char in set(s):  # Only iterate over unique characters
            first, last = s.find(char), s.rfind(char)  # Get first and last occurrence
            
            if first < last:  # Ensure there is a middle section
                unique_middle = set(s[first + 1:last])  # Get unique middle characters
                result += len(unique_middle)  # Each unique Y forms (X, Y, X)
        
        return result
