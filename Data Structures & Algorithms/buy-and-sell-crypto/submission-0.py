class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        for i, p in enumerate(prices):
            if p < prices[buy]:
                buy = i
            elif p - prices[buy] > profit:
                profit = p - prices[buy]
        return profit