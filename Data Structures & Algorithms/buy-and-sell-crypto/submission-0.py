class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for p in range(0, len(prices)):
            for p2 in range(p+1, len(prices)):
                curr_profit = prices[p2] - prices[p]

                if(curr_profit > profit):
                    profit = curr_profit

        return profit

        