# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
from functools import cache

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prices = [100000] + prices + [0]
        valley_indexes = []
        peak_indexes = []
        valley_control = [lambda a, b: a > b, valley_indexes]
        peak_control = [lambda a, b: a < b, peak_indexes]
        control = valley_control
        for index, price in enumerate(prices[1:]):
            if control[0](price, prices[index]):
                control[1].append(index)
                control = peak_control if control == valley_control else valley_control
        extr_len = len(valley_indexes)

        @cache
        def cal_max_profit(valley_index, peak_index, end_index):
            if peak_index == end_index:
                return 0
            if valley_index == end_index:
                return 0
            max_profit = max(0, prices[peak_indexes[peak_index]] - prices[valley_indexes[valley_index]])
            peak_index += 1
            return max(
                max_profit,
                cal_max_profit(valley_index, peak_index, end_index),
                cal_max_profit(valley_index + 1, peak_index, end_index)
            )

        two_deals_profit = cal_max_profit(0, 0, extr_len)
        for i in range(1, extr_len):
            two_deals_profit = max(two_deals_profit, cal_max_profit(0, 0, i) + cal_max_profit(i, i, extr_len))
        return two_deals_profit

solution = Solution()
print(solution.maxProfit([1,2,3,4,5]))
