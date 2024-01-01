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
        def cal_min_price(start_index, end_index):
            min_price = prices[valley_indexes[start_index]]
            if start_index == end_index:
                return min_price
            return min(min_price, cal_min_price(start_index + 1, end_index))

        def cal_max_profit(start_index, end_index):
            max_profit = 0
            for peak_index in range(start_index, end_index):
                max_profit = max(max_profit, prices[peak_indexes[peak_index]] - cal_min_price(start_index, peak_index))
            return max_profit

        two_deals_profit = 0
        for i in range(0, extr_len):
            two_deals_profit = max(two_deals_profit, cal_max_profit(0, i) + cal_max_profit(i, extr_len))
        return two_deals_profit

solution = Solution()
print(solution.maxProfit([3,3,5,0,0,3,1,4]))
