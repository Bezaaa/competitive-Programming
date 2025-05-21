class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_t = list(t)
        list_s = list(s)
        return sorted(list_s) == sorted(list_t)