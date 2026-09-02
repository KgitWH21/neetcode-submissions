class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for current_price in prices:
            lowest_price = min(lowest_price, current_price)

            current_profit = current_price - lowest_price
            max_profit = max(max_profit, current_profit)
        
        return max_profit