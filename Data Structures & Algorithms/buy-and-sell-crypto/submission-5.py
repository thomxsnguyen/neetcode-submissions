class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, maxProfit = 0, 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            maxProfit = max(maxProfit, prices[right] - prices[left])
        return maxProfit