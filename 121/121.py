class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in prices:
            if buy < i:
                price = i - buy
                profit = max(profit, price)
                
            else:
                buy = i
        return profit

            