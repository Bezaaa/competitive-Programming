class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n +1):
            j = i+n
            if haystack[i:j] == needle:
                return i
        return -1

        