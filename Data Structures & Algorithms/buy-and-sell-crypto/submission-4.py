class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        best = 0
        n = len(prices)

        for right in range(1,n):
            if prices[right] - prices[left] > 0:
                best = max(best, abs(prices[left] - prices[right]))
                right += 1

            elif prices[right] - prices[left] < 0:
                left = right

        return best

