class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        freqMap = {}

        if len(s1) > len(s2): return False

        for s in s1:
            freqMap[s] = freqMap.get(s, 0) + 1

        windowMap = {}

        for i in range(len(s1)):
            windowMap[s2[i]] = windowMap.get(s2[i], 0) + 1
        
        for right in range(len(s2) - len(s1)):
            if windowMap == freqMap:
                return True
            
            windowMap[s2[left]] -= 1

            char = s2[left + len(s1)]
            windowMap[char] = windowMap.get(char, 0) + 1

            if windowMap[s2[left]] == 0:
                del windowMap[s2[left]]

            left += 1
        
        
        
        



        return False

        