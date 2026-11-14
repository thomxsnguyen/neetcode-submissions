class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        s = ''
        for i in range(min(len(word1), len(word2))):
            s += word1[i]
            s += word2[i]
        
        print(s)
        