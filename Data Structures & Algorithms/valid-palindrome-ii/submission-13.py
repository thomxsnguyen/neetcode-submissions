class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        count = 0
        while left < right:
            if s[left] != s[right]:
                count += 1
            print(s[left], s[right])
            left += 1
            right -= 1
            
        if count > 1:
            return False

        return True