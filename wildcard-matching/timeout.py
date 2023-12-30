# https://leetcode.cn/problems/wildcard-matching/
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub(r'\?', '.', p)
        p = re.sub(r'\*+', '.*', p)
        return re.match(f'^{p}$', s) is not None

solution = Solution()
print(solution.isMatch('abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb', '**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb'))