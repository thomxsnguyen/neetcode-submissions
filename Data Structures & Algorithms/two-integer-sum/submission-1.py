class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}


        for idx, val in enumerate(nums):
            complement = target - val
            if complement in ht:
                return [idx, ht[complement]]
            ht[val] = idx
        
        