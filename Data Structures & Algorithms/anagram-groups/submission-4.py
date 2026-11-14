class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict 
        output = []
        anagrams = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        for key, value in anagrams.items():
            output.append(value)
        return output