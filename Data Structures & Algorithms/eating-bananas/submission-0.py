class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        l, r = 1, max(piles)

        res = max(piles)

        while l <= r:
            mid = l + ((r - l) // 2)
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)
                
            if hours > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        
        return res
