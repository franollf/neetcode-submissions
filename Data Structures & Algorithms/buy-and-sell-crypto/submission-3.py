class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(len(prices)):
            ## if its graeater than get that difference and change the max
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

            ## if the prices[r] is less than the prices[l] then we should BUY at that point
            elif prices[l] > prices[r]:
                l = r
            
        return maxP