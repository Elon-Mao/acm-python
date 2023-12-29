# https://leetcode.cn/problems/trapping-rain-water/

class Solution:
    def trap(self, height: list[int]) -> int:
        max_bar = 0
        levels = []
        for bar in height:
            max_bar = max(bar, max_bar)
            levels.append(max_bar)
        capacity = max_bar = 0
        for bar in height[::-1]:
            max_bar = max(bar, max_bar)
            capacity += min(max_bar, levels.pop()) - bar
        return capacity

solution = Solution()
print(solution.trap([4, 2, 0, 3, 2, 5]))
