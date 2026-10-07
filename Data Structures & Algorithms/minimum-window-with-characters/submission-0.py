class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # what characters do t require?
        # how many of those characters are currently inside our window?

        left = 0
        window, need = {}, {}
        have = 0
        needCount = len(t)

        
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        for right in range(len(s)):
            # add right t our window
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            
            while have == needCount:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                
                windows[s[left]] -= 1

                if s[left] in need and windows[s[left]] < need[s[left]]:
                    have -= 1

                left += 1
        
        return s[left:left + minlength]