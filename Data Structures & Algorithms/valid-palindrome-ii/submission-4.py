class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while s[left].isalnum():
                left += 1
            while s[right].isalnum():
                right -= 1
            
            if s[left] != s[right]:
                return False
        
        return True