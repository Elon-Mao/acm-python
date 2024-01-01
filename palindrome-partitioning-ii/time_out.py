# https://leetcode.cn/problems/palindrome-partitioning-ii/
from functools import cache


class Solution:
    def minCut(self, s: str) -> int:

        @cache
        def cal_min_cut(sub_str):
            if sub_str == sub_str[::-1]:
                return 0
            min_cut = 2000
            for i in range(1, len(sub_str)):
                min_cut = min(min_cut, cal_min_cut(sub_str[:i]) + cal_min_cut(sub_str[i:]))
            return min_cut + 1

        return cal_min_cut(s)


solution = Solution()
print(solution.minCut('apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp'))
