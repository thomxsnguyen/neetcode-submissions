class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = ()

        for num in nums:
            if num in hashset:
                return False
            hashset.add(num)
        
        return True