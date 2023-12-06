"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


def maxProfitBruteForce(prices):
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


def maxProfitDynamicProgramming(prices):
    if not prices or len(prices) < 2:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


def maxProfitMemory(prices):
    if not prices or len(prices) < 2:
        return 0

    # Create an array of daily changes in prices
    diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

    # Initialize variables to keep track of current profit and max profit
    current_profit = max_profit = 0

    # Iterate through the differences array
    for d in diff:
        # Update current profit by adding the current difference if positive, otherwise reset to 0
        current_profit = max(0, current_profit + d)

        # Update max profit if current profit becomes greater than max profit
        max_profit = max(max_profit, current_profit)

    return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return maxProfitBruteForce(prices)
        # return maxProfitMemory(prices)
        return maxProfitBruteForce(prices)


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
# print(s.maxProfit([7, 6, 4, 3, 1]))
