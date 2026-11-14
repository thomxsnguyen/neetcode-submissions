class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            key = sorted(s)
            anagrams[key] = anagrams.get(key, []).append(key)
        
        print(anagrams)