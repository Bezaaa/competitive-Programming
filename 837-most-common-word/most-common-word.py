class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hash_map = {}
        words = re.sub(r"[^\w\s]", " ", paragraph).split()    
 
        print(words)

        for word in words:
            word = word.lower()
           
            hash_map[word] = hash_map.get(word , 0) + 1
        freq = max((item for item in hash_map.items() if item[0] not in banned),
               key=lambda x: x[1])

        return freq[0]
      