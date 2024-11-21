class Solution(object):
    def maxProfit(self, prices):
        profit=0
        buy=float('inf')
        for price in prices:
            if (price<buy):
                buy=price
            else:
                profit=max(profit,price-buy )
        return profit 