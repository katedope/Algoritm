class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth_descent = [1] * len(prices)
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                smooth_descent[i] += smooth_descent[i - 1]

        return sum(smooth_descent)