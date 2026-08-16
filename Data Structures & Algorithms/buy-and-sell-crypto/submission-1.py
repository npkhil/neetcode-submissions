class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxprofit = 0
        for p in prices:
            minbuy = min(minbuy, p)
            maxprofit = max(maxprofit, p - minbuy)
        return maxprofit