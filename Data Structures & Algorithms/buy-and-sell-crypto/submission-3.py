class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = buy = sell = 0

        while sell < len(prices):
            profit = max(profit, prices[sell] - prices[buy])
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
        
        return profit