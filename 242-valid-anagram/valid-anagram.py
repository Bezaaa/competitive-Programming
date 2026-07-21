class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char , 0) +1
        for char in t:
            if char not in hash_map:
                return False
            if char in hash_map:
                hash_map[char]-=1
                if hash_map[char] <0:
                    return False
        for val in hash_map.values():
            if val != 0 :
                return False
        return True
        