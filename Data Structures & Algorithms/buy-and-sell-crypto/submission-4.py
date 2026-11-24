class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        final=0
        for i in range(len(prices)):
            max_sell = max(prices[i:])
            profit = max_sell - prices[i]
            if final < profit:
                final = profit
        return final