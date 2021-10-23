"""
Time complexity : O(n). Only a single pass is needed.
Space complexity : O(1). Only two variables are used.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            
            if profit > max_profit:
                max_profit = profit
            if buy > prices[i]:
                buy = prices[i]
        
        return max_profit

"""
EPI solution
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far, max_profit = float('inf'), 0
        
        for price in prices:
            max_profit_sell_today = price - min_price_so_far
            max_profit = max(max_profit, max_profit_sell_today)
            min_price_so_far = min(min_price_so_far, price)

        return max_profit
            
