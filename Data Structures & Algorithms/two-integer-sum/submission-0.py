class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i, v in enumerate(nums):
            complement = target - v
            if complement in indices:
                return [indices[complement], i]
            indices[v] = i

        return []