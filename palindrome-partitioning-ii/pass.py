# https://leetcode.cn/problems/palindrome-partitioning-ii/
class Solution:
    def minCut(self, s: str) -> int:
        s_len = len(s)
        min_cut_list = [2000] * s_len + [-1]

        def update_min_cut(left_index, right_index):
            while left_index >= 0 and right_index < s_len:
                if s[left_index] != s[right_index]:
                    return
                min_cut_list[right_index] = min(min_cut_list[right_index], min_cut_list[left_index - 1] + 1)
                left_index -= 1
                right_index += 1

        for i in range(0, s_len):
            min_cut_list[i] = min(min_cut_list[i], min_cut_list[i - 1] + 1)
            update_min_cut(i - 1, i)
            update_min_cut(i - 1, i + 1)
        return min_cut_list[s_len - 1]


solution = Solution()
print(solution.minCut('aab'))
