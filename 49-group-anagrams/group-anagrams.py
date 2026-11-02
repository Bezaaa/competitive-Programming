class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
         
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

       
            key = tuple(count)

      
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(word)

       
        return list(hash_map.values())


        