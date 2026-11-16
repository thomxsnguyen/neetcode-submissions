class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        # "zxyzxyz"
        # z: 1 (longest = 1)
        # z: 1, x:1, (longest = 2)
        # z: 1, x:1, y:1 (longest = 3)
        # z: 2, x:1, y: 1) do not update longest, del z, decrease length by 1
        # z: 1, x:2, y:1) do not update longest, del x, decrease length by 1
    
        left, longest = 0, 0
        charSet = set()

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])

            longest = max(longest, right - left + 1)
        return longest
        

        
