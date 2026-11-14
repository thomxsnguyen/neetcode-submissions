class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        position = 0

        while position < len(nums):
            print(position, nums[position])
            if position >= len(nums) - 1:
                return True
            if nums[position] == 0:
                return False
            position += nums[position]
        return True