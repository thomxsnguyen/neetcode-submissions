class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            left += 1
            right += 1
            
            if s[left] != s[right]:
                return False
        
        return True