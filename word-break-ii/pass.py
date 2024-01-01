# https://leetcode.cn/problems/word-break-ii/description/
from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        end_index = len(s) - 1

        @cache
        def word_break(start_index):
            word = ''
            sentences = []
            for i in range(start_index, end_index):
                word += s[i]
                if word in word_set:
                    sub_sentences = word_break(i + 1)
                    for sub_sentence in sub_sentences:
                        sentences.append(f'{word} {sub_sentence}')
            word += s[end_index]
            if word in word_set:
                sentences.append(word)
            return sentences

        return word_break(0)


solution = Solution()
print(solution.wordBreak('catsanddog', ["cat","cats","and","sand","dog"]))