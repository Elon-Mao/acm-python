# https://leetcode.cn/problems/dungeon-game/submissions/

class Solution:

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        class HpDict:
            def __init__(self):
                self.hp_dict = {}

            def add(self, hp, full_hp):
                if hp in self.hp_dict:
                    self.hp_dict[hp] = min(self.hp_dict[hp], full_hp)
                else:
                    self.hp_dict[hp] = full_hp

            def affect(self, effect):
                new_dict = HpDict()
                for hp in self.hp_dict:
                    new_hp = hp + effect
                    if new_hp > 0:
                        new_dict.add(new_hp, self.hp_dict[hp])
                    else:
                        new_dict.add(1, self.hp_dict[hp] + 1 - new_hp)
                return new_dict

            def concat(self, hp_dict):
                for hp in hp_dict:
                    self.add(hp, hp_dict[hp])

            def get_min(self):
                min_full_hp = float('inf')
                for hp in self.hp_dict:
                    min_full_hp = min(min_full_hp, self.hp_dict[hp])
                return min_full_hp

        max_i = len(dungeon)
        max_j = len(dungeon[0])
        first_dict = HpDict()
        first_dict.add(1, 1)
        hp_dict_list = [first_dict.affect(dungeon[0][0])]
        for j in range(1, max_j):
            hp_dict_list.append(hp_dict_list[j - 1].affect(dungeon[0][j]))
        for i in range(1, max_i):
            hp_dict_list[0] = hp_dict_list[0].affect(dungeon[i][0])
            for j in range(1, max_j):
                hp_dict_list[j].concat(hp_dict_list[j - 1].hp_dict)
                hp_dict_list[j] = hp_dict_list[j].affect(dungeon[i][j])
        return hp_dict_list[max_j - 1].get_min()

solution = Solution()
print(solution.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))