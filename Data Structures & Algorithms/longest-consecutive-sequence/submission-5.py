class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        
        for num in nums:
            #if num is not starting point we skip, otherwise length = 1
            if num - 1 not in nums:
                length = 1
                # iterate through set until length is not in nums consecutively.
                while num + length in nums:
                    length += 1
                # update longest if current length is greater than longest
                longest = max(longest, length)
        return longest