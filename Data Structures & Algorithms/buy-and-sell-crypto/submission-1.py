class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maximumProfit = 0

        # max(maximumProfit, prices[l] - prices[r])

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maximumProfit = max(maximumProfit, prices[l] - prices[r])
            r += 1

