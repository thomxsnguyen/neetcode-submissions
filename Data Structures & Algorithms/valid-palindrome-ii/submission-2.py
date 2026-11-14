class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)

        while left < right:
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1
            
            if s[left] != s[right]:
                return False
        
        return True