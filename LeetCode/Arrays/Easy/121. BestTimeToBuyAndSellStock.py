"""
------------------------------------------------------------------------------------------------------------------------------------------------
121. Best Time to Buy and Sell Stock (EPI)(Blind)(LeetCode)
------------------------------------------------------------------------------------------------------------------------------------------------

You are given an ARRAY prices where "prices[i]" is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough
------------------------------------------------------------------------------------------------------------------------------------------------

This solution will require keeping track of the MAX profit, as we are iterating through the list. "profit" will be equaled to the current price
subtracted by the minumum price we bought at. Once we have calculated that, we have to do two checks. If "profit" is greater than the "max_profit", that 
means we have a new max therefore we change the "max_profit" to reflect the new highest value, that will be maintained, until there is a higher
profit. The next check will be to see if the price we bought at "buy" is greater than the todays price (the price we are currently looking at). 
If todays price is smaller, we will change the buy to the smallest price to see if we can create a higher profit as we go through the list. 
Then the loop will continue until we have reached the end of the list. 

Ex. prices = [7,1,5,3,6,4]

buy   |   max_profit   |   profit   |   i   | 
7             0                         
1             0              -6         1
1             4              4          2
1             4              2          3
1             5              5          4
1             5              3          5

Return: 5

Time complexity : O(n). Only a single pass is needed.
Space complexity : O(1). Only two variables are used.
------------------------------------------------------------------------------------------------------------------------------------------------
"""

def maxProfit(self, prices: List[int]) -> int:
    res = 0
    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
    return res

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

# EPI Solution
def maxProfit(self, prices: List[int]) -> int:
    min_price_so_far, max_profit = float('inf'), 0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit
