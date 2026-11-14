class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}


        for idx, val in enumerate(nums):
            complement = target - val
            if complement in ht:
                return [ht[complement], idx]
            ht[val] = idx
        
