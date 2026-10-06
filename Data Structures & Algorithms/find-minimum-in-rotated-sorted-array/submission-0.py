class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = l + ((r - l) // 2)

            if nums[mid] > nums[r]:
                # drop on the right
                l = mid + 1
                
            elif nums[mid] < nums[r]:
                # sorted on the right
                r = mid
            
        return nums[l]
