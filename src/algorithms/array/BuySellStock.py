from typing import List


class BuySellStock:

    def __init__(self):
        pass

    @staticmethod
    def max_profit(prices: List[int]) -> int:
        max_profit = 0
        for index in range(1, len(prices)):
            max_profit = max_profit + max(0, prices[index] - prices[index - 1])
        return max_profit

    def __repr__(self):
        return 'BuySellStock'
