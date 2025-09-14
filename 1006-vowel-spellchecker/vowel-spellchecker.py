class Solution(object):
    def spellchecker(self, wordlist, queries):
        # Helper to normalize vowels
        def normalize(word):
            vowels = set("aeiou")
            return "".join("*" if c in vowels else c for c in word.lower())
        lowercase_map ={}
        vowel_map = {}
        res = []
        for word in wordlist:
            lower = word.lower()
            normalized = normalize(word)
            if lower not in lowercase_map:
                lowercase_map[lower] = word
            if normalized not in vowel_map:
                vowel_map[normalized] = word
        for query in queries:
            if query in wordlist:
                res.append(query)
            elif query.lower() in lowercase_map:
                res.append(lowercase_map[query.lower()])
            elif normalize(query) in vowel_map:
                res.append(vowel_map[normalize(query)])
            else:
                res.append("")
        return res