# https://leetcode.cn/problems/distinct-subsequences/
from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def cal_ways(s_sub, t_sub):
            if len(t_sub) > len(s_sub):
                return 0
            ways = cal_ways(s_sub[1:], t_sub)
            if s_sub[0] == t_sub[0]:
                ways += 1 if len(t_sub) == 1 else cal_ways(s_sub[1:], t_sub[1:])
            return ways

        return cal_ways(s, t)

solution = Solution()
print(solution.numDistinct('babgbag', 'bag'))