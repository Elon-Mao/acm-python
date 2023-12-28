# # https://leetcode.cn/problems/regular-expression-matching/
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub(r'\*+', '*', p)
        return re.match(f'^{p}$', s) is not None

solution = Solution()
print(solution.isMatch('abc', 'a***abc'))