class Solution(object):
    def maxProfit(self, prices):
        buyingPointer = 0
        sellingPointer = 1
        maxProfit = 0

        while sellingPointer < len(prices):
            if prices[sellingPointer] > prices[buyingPointer]:
                profit = prices[sellingPointer] - prices[buyingPointer]
                maxProfit = max(maxProfit, profit)
            else:
                buyingPointer = sellingPointer
            sellingPointer += 1
        return maxProfit