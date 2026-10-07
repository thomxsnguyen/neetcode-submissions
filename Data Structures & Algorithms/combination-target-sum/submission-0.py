class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        total = 0

        def backtrack(i, total):
            # base case
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target or i >= len(nums):
                return

            subset.append(nums[i])
            backtrack(i, total + nums[i])

            subset.pop()
            backtrack(i + 1, total)
        
        backtrack(0, 0)
        return res

            


