# https://leetcode.cn/problems/scramble-string/
from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def is_scramble(s1, s2):
            s_len = len(s1)
            if s_len == 1:
                return s1 == s2
            for i in range(1, s_len):
                s1_0 = s1[:i]
                s1_1 = s1[i:]
                if is_scramble(s1_0, s2[:i]) and is_scramble(s1_1, s2[i:]):
                    return True
                if is_scramble(s1_1, s2[:-i]) and is_scramble(s1_0, s2[-i:]):
                    return True
            return False

        return is_scramble(s1, s2)

solution = Solution()
print(solution.isScramble('great', 'rgeat'))