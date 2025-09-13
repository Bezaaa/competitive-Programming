class Solution(object):
    def maxFreqSum(self, s):
        """
    lower case English letters
    find the vowel with maximum frequency
    find the consonant with maximum frequency
    return the sum 
        """
        vowels = ['a','e','i','o','u']
        vowel_hash_map  = {}
        consonant_hash_map = {}
        for i in s:
            if i in vowels:
                vowel_hash_map[i] = vowel_hash_map.get(i,0) + 1
            else:
                consonant_hash_map[i] = consonant_hash_map.get(i,0) + 1
        if not consonant_hash_map and not vowel_hash_map:
            return 0
        if not consonant_hash_map :
            return max(vowel_hash_map.values())
        if not vowel_hash_map : 
            return max(consonant_hash_map.values())
        freq_vowel = max(vowel_hash_map.values())
        freq_cons = max(consonant_hash_map.values())
        return freq_cons + freq_vowel

        