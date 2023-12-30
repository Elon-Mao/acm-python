# https://leetcode.cn/problems/wildcard-matching/
import re
from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = list(s)
        p = list(re.sub(r'\*+', '*', p))
        s_len = len(s)
        p_len = len(p)

        @cache
        def is_match(s_index, p_index):
            if p_index == p_len:
                return s_index == s_len
            p_item = p[p_index]
            if s_index == s_len:
                return p_index == p_len - 1 and p_item == '*'
            if p_item == '?':
                return is_match(s_index + 1, p_index + 1)
            if p_item == '*':
                return is_match(s_index + 1, p_index + 1) or is_match(s_index + 1, p_index) or is_match(s_index, p_index + 1)
            if p_item == s[s_index]:
                return is_match(s_index + 1, p_index + 1)
            return False

        return is_match(0, 0)

solution = Solution()
print(solution.isMatch('abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb', '**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb'))