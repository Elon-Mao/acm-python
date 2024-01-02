# # https://leetcode.cn/problems/word-ladder-ii/
from functools import cache
from typing import List


class WordNode:
    def __init__(self, word):
        self.word = word
        self.pair_set = set()

    def add_pair(self, pair):
        self.pair_set.add(pair)


@cache
def get_node(word):
    return WordNode(word)


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def is_adjacent(word1, word2):
            differs = 0
            for i in range(0, word_len):
                if word1[i] != word2[i]:
                    differs += 1
                    if differs > 1:
                        return False
            return differs == 1

        def get_sequences(word_node):
            if word_node.word == endWord:
                return [[endWord]]
            sequences = []
            for pair in word_node.pair_set:
                sequences += get_sequences(pair)
            for sequence in sequences:
                sequence.insert(0, word_node.word)
            return sequences

        word_len = len(beginWord)
        word_set = set(wordList)
        last_nodes = {get_node(beginWord)}
        while len(last_nodes) > 0:
            used_set = set()
            new_nodes = set()
            for node in last_nodes:
                for word in word_set:
                    if not is_adjacent(node.word, word):
                        continue
                    new_node = get_node(word)
                    new_nodes.add(new_node)
                    node.add_pair(new_node)
                    used_set.add(word)
            if endWord in used_set:
                return get_sequences(get_node(beginWord))
            for word in used_set:
                word_set.remove(word)
            last_nodes = new_nodes
        return []


solution = Solution()
print(solution.findLadders('aaaaa', 'ggggg',
                           ['aaaag',
                            'aaagg',
                            'aabgg',
                            'abbgg',
                            'bbbgg',
                            'bbbbg',
                            'cbbbg',
                            'ccbbg',
                            'cccbg',
                            'ccccg',
                            'cccgg',
                            'ccggg',
                            'cgggg',
                            'ggggg']))


