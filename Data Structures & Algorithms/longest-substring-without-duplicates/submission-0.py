class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            if s[right] not in charSet:
                charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
        return maxLength
