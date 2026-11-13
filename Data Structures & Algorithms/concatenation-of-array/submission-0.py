class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)
        for i in range(len_nums):
            nums.append(nums[i])
        
        return nums