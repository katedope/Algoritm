class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                cur_max += prices[i] - prices[i - 1]

        return cur_max