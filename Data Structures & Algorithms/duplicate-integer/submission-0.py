class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            left, right = 0, len(nums) - 1
            middle = (left + right) // 2
            while left <= right:
                if nums[middle] < x:
                    left = middle + 1
                elif nums[middle] > x:
                    right = middle -1
                else:
                    return False
        return True