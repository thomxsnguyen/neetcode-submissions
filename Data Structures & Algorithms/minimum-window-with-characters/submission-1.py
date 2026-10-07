class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # what characters do t require?
        # how many of those characters are currently inside our window?

        minLength = float('inf')
        left, have, start = 0, 0, 0
        window, need = {}, {}

        
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        needCount = len(need.keys())
        
        for right in range(len(s)):
            # add right t our window
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            
            while have == needCount:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    start = left
                
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1
        if minLength == float('inf'):
            return ''
        return s[start:start + minLength]