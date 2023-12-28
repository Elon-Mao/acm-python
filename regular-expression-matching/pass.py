# # https://leetcode.cn/problems/regular-expression-matching/
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def cache_decorator(func):
            cache = {}

            def wrapper(*args):
                key = args
                if key in cache:
                    return cache[key]
                result = func(*args)
                cache[key] = result
                return result

            return wrapper

        p_mixes = re.split(r'(?!\*)', p)[1:-1]
        s_chars = list(s)
        p_len = len(p_mixes)
        s_len = len(s_chars)

        def can_finish(j):
            for i in range(j, p_len):
                if len(p_mixes[i]) == 1:
                    return False
            return True

        def is_char_equal(s_char, p_char):
            return p_char == '.' or s_char == p_char

        @cache_decorator
        def is_match(i, j):
            if j == p_len:
                return i == s_len
            if i == s_len:
                return can_finish(j)
            has_aster = len(p_mixes[j]) != 1
            if is_char_equal(s_chars[i], p_mixes[j][0]):
                return is_match(i + 1, j + 1) or has_aster and (is_match(i + 1, j) or is_match(i, j + 1))
            else:
                return has_aster and is_match(i, j + 1)

        return is_match(0, 0)

solution = Solution()
print(solution.isMatch('abc', 'a***abc'))