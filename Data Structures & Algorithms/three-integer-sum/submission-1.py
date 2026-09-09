class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and (val == nums[idx - 1]):
                continue
            
            l, r = idx + 1, len(nums) - 1

            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r -= 1
                else:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    while (l < r) and (nums[l] == nums[l - 1]):
                        l += 1
        
        return result