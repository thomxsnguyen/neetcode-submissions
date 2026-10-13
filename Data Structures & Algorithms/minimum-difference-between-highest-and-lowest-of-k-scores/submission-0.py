class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        difference = float('inf')
        for r in range(k - 1, len(nums)):
            difference = min(difference, nums[r] - nums[l])
            l += 1
        return difference